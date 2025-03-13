from Game import Game
from Player import Player
def run():

    game = Game()

    game_players = [Player("Andre", "Onana", False, 64,464, "Manchester United", dribbling=5)
        , Player("Patrick", "Dorgu", False, 464,101, "Manchester United"),
                    Player("Noussair", "Mazraoui", False, 333, 227, "Manchester United", position="CB"),
                    Player("Matthijs", "de Ligt", False, 311,454, "Manchester United", position="CB"),
                    Player("Leny", "Yoro", False, 334,722, "Manchester United"),
                    Player("Casemiro", "", False, 465,319, "Manchester United"),
                    Player("Diego", "Dalot", False, 400,803, "Manchester United"),  # Originally 37
                    Player("Alejandro", "Garnacho", False, 639, 774, "Manchester United"),
                    Player("Bruno", "Fernandes", False, 451,579, "Manchester United"),  # Originally 27
                    Player("Joshua", "Zirkzee", False, 612,163, "Manchester United"),
                    Player("Rasmus", "Hojlund", False, 671,430, "Manchester United", kickOff=False, passing=10),

                    Player("Ederson", "Morares", False, 1635,460, "Manchester City", speed=12)
        , Player("Matheus", "Nunes", False, 1372,95, "Manchester City", speed=13, workRate=5),
                    Player("Abdukodir", "Khusanov", False, 1360,316, "Manchester City", speed=13),
                    Player("Rueben", "Dias", False, 1358,514, "Manchester City", speed=12),
                    Player("Josko", "Gvardiol", False, 1356,760, "Manchester City", speed=20, workRate=4),
                    Player("Mateo", "Kovacic", False, 1169,359, "Manchester City", speed=13),
                    Player("Nico", "Gonzalez", False, 1193, 517, "Manchester City", speed=13),
                    Player("Savinho", "", False, 1067, 112, "Manchester City", speed=18),
                    Player("Omar", "Marmoush", False, 994,450, "Manchester City", speed=18),
                    Player("Jérémy", "Doku", False, 1107,840, "Manchester City", speed=14),
                    Player("Erling", "Haaland", True, 859,454, "Manchester City", kickOff=True, speed=17, position="ST")]

    game.run(game_players)



if __name__ == '__main__':
    run()


