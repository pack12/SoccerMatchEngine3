import pygame
from Ball import Ball
from Player import PlayerData
from PlayerStates import AIState
class Game:
    def __init__(self):

        self.width = 1700
        self.height = 925
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Soccer Sim")
        self.clock = pygame.time.Clock()
        self.running = True
        self.debug = True

    """Soccer surf is created here"""

    def create_field(self):

        self.soccer_surf = pygame.image.load("Images/Soccer_Field_Transparant.svg.png")
        self.soccer_surf = pygame.transform.scale(self.soccer_surf, (self.width - 780, 1700))
        self.soccer_surf = pygame.transform.rotate(self.soccer_surf, 90)

        return self.soccer_surf

    def check_events(self, players, playerData):

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f'{pygame.mouse.get_pos()}')
                # pygame.draw.circle(self.win,(0,0,255),pygame.mouse.get_pos(),3.0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    playerData.get_player_rects(players)


            elif event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for i in players:
                if i.hasBall:
                    i.x -= 7
        elif keys[pygame.K_RIGHT]:
            for i in players:
                if i.hasBall:
                    i.x += 7
        elif keys[pygame.K_DOWN]:
            for i in players:
                if i.hasBall:
                    i.y += 7
        elif keys[pygame.K_UP]:
            for i in players:
                if i.hasBall:
                    i.y -= 7


    def run(self, players):
        soccer_field = self.create_field()
        playerData = PlayerData()

        ball = Ball(players)
        playerData.get_player_rects(players)
        print(playerData.playerRects)
        angle = 0
        player_frame = 0

        while self.running:

            self.check_events(players, playerData)

            #Move Players

            # RENDER YOUR GAME HERE
            self.win.blit(soccer_field, (0, 0))
            playerData.get_player_rects(players)
            playerData.draw_players(self.win,players)

            for i in players:
                if i.fullName == "Erling Haaland":

                    # print(i.state)
                    if i.state == "Idle" and i.initial_scan:

                        i.update_state(AIState.FIND_DRIBBLE_LANE)
                    elif i.state == AIState.FIND_DRIBBLE_LANE:
                        i.scan_in_front(playerData.playerRects, self.win)
                        if i.completed_scan:
                            # i.update_state(AIState.IDLE)
                            #Have player make decision where to go with the ball
                            i.choose_dribble_lane(playerData, self.win)
                            i.update_state(AIState.DRIBBLING)
                    elif i.state == AIState.DRIBBLING:
                        # print("Player is dribbling")
                        i.move(i.chosen_dribble_lane[player_frame][0], i.chosen_dribble_lane[player_frame][1])

                        if player_frame < len(i.chosen_dribble_lane) - 4:
                            player_frame += 4

                        if player_frame == len(i.chosen_dribble_lane) - 4:
                            # print("Player completed dribble")
                            i.update_state(AIState.COMPlETED_DRIBBLE)
                    elif i.state == AIState.COMPlETED_DRIBBLE:
                        i.initial_scan = True
                        i.state = AIState.IDLE
                        i.completed_scan = False
                        player_frame = 0
                        i.list_of_potential_lanes = []
                        i.chosen_dribble_lane = []

            ball.draw_ball(self.win, players, playerData)
            pygame.display.flip()  # Update Display

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

