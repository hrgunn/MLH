from view import class ClassName(game):

class Game():
    """docstring for Game"""
    def __init__(self, arg):
        super(Game, self).__init__()
        self.mission = []
        self.player = None
        self.view = View()


#Damn son where'd you find this?

class mission(object):
    """docstring for mission"""
    def __init__(self, arg):
        super(mission, self).__init__()
        self.arg = arg
        
    def start(self, player):
        self.player = player
        self.view.mission_description(self.name)

    """this will allow user to sign up and log in """
    def __init__(self,name):
        super(user, self).__init__()
        self.name = name
        #there is no password provided
        input ("What yo name be?")
            return()

    def __init__(self.lucky):
        input = ("Would you like a trick or treat?")
        #user will write trick and specific names output
        #user will write treat and specific names output
        choice = input ["Nothing [0], Trick [1], Treat [2]"]
            if "Nothing" end game
            if "Trick", select.name.Trick
            if "Treat", select.name.Treat

            #names of the Trick and Treat hoeses
        choice_trick = input ["Derpy Hooves [0], Princess Luna [1], Discord [3]"]
        choice_treat = input ["Rainbow Dash [0], Rarity [2], Sunset Shimmer [3]"]

    def __init__(self.ready):
        choice = input("Will you be providing insurance?")
            if ["No" [0]], end game
                elif ("You mean Yes?")
            if ["Yes" [1]], continue to patdown

    def __init__(self.pay)
        choice = input("Whur dat money?")
            if [credit card [0]]:
            pass
            if [cash [1]]:
            pass
            if [coins [2]]:
            end game

    def __init__(self.ready)
        
        choice = input("Ready for more?")
            if condition:
                pass ["Yes" [0]]
                Return True
            else ("No" [1])
                elif Game Over


game = Game()
missions = []
missions.append(Mission("Would you like a trick or treat?", ["Nothing [0], Trick [1], Treat [2]"])
missions.append(Mission("Pick your trick", ["Derpy Hooves [0], Princess Luna [1], Discord [3]"])
missions.append(Mission("Pick your treat", ["Rainbow Dash [0], Rarity [2], Sunset Shimmer [3]")
missions.append(Mission("Will you be providing insurance? ["No" [0], ["Yes" [1]])
missions.append(Mission("Whur dat money?" [credit card [0],[cash [1],[coins [2]])
missions.append(Mission("Ready for more?")

game.load_missions(missions)
game.start()
game.play()
game.credit()