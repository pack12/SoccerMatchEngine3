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
                    if i.state == "Idle":

                        i.update_state(AIState.FIND_DRIBBLE_LANE)
                    elif i.state == AIState.FIND_DRIBBLE_LANE:
                        i.scan_in_front(playerData.playerRects)
                        # print(f'X: {i.player_vision_rect.x} Y: {i.player_vision_rect.y} Width: {i.player_vision_rect.width} Height: {i.player_vision_rect.height}')



            ball.draw_ball(self.win, players, playerData)
            pygame.display.flip()  # Update Display

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

