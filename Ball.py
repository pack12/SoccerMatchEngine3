import pygame
import math
class Ball:
    def __init__(self, players):
        self.currentIndex = 0
        self.playerAttached = None
        for i in players:
            if i.hasBall== True and i.Team == "Manchester City":
                self.x = i.x - 3
                self.y = i.y
            elif i.hasBall == True and i.Team == "Manchester United":
                self.x = i.x + 3
                self.y = None
    def create_ball(self):
        ball_surf = pygame.image.load("Images/soccerBall.png")
        ball_surf = pygame.transform.scale(ball_surf,(20,16))
        ball_surf.set_colorkey("Black")
        return ball_surf

    def update_index(self,futureIndex):
        self.currentIndex = futureIndex
    def draw_ball(self,win,players, player_data):
        plaayer = None
        ball_surf = self.create_ball()
        ball_rect = pygame.Rect(self.x, self.y, ball_surf.get_width(), ball_surf.get_height())

        for i in players:
            if i.hasBall== True and i.Team == "Manchester City":

                center_x = player_data.playerRects[i].x + (player_data.playerRects[i].width) / 2
                center_y = player_data.playerRects[i].y + (player_data.playerRects[i].height) / 2
                plaayer = i

                new_x, new_y = self.rotate_point((center_x - 20, center_y), (center_x, center_y), i.angle)

                ball_rect.center = (new_x,new_y)


            elif i.hasBall == True and i.Team == "Manchester United":
                # playerRect = playerData.playerRects[i]
                self.x = i.x + 3
                self.y = i.y


        win.blit(ball_surf, ball_rect)
        pygame.draw.rect(win,(255,0,0),ball_rect,2)




    def rotate_point(self,point, pivot, angle):
        """Rotate a point around a pivot by an angle (in degrees)."""
        x, y = point
        px, py = pivot
        radians = math.radians(angle)

        x_new = px + (x - px) * math.cos(radians) - (y - py) * math.sin(radians)
        y_new = py + (x - px) * math.sin(radians) + (y - py) * math.cos(radians)

        return x_new, y_new


    def rotate_point2(self, pivot, radius, angle):
        """Rotate a point around a pivot by an angle (in degrees) while keeping a fixed radius."""
        radians = math.radians(angle)
        x_new = pivot[0] + radius * math.cos(radians)
        y_new = pivot[1] + radius * math.sin(radians)
        return x_new, y_new

    def distance(self,point1, point2):
        """Calculate the Euclidean distance between two points in 2D or 3D space."""
        if len(point1) != len(point2):
            raise ValueError("Both points must have the same number of dimensions")

        return math.sqrt(sum((p2 - p1) ** 2 for p1, p2 in zip(point1, point2)))


