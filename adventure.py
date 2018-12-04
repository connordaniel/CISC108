"""
Text Adventure Game
An adventure in making adventure games.

Refer to the instructions on Canvas for more information.

"""
__author__ = "Connor Daniel"
__version__ = 2
class Player:

    def __init__(self, given_location, knife, identity, given_list):
        self.location = given_location
        self.has_knife = knife
        self.knows_killer = identity
        self.evidence = given_list

class World:
    """ 
Attributes: 
    game_status (str): Whether the game 
    is in progress or has ended. Either "playing", 
    "won", or "lost". 

    player (Player): The player character's info. 

    killer_caught (bool): whether or not the killer
    has been apprehended. Determines the end of the game
""" 
    def __init__(self):
        self.game_status = "playing"
        self.player = Player("office", False, False, [""])
        self.killer_caught = False
    def is_done(self):
        if self.game_status == "won" or self.game_status == "lost" or self.game_status == "quit":
            return True
        else:
            return False
    def is_good(self):
        return True
    def render(self):
        message = ""
        message += self.render_location()
        return message
    def render_location(self)
    def is_input_good(self, inputString):
        if inputString == "win" or inputString == "lose" or inputString == "quit":
            return True
        else:
            return False
    def process(self, inputString):
        if inputString == "win":
            self.game_status = "won"
        elif inputString == "play":
            self.game_status = "playing"
        elif inputString == "quit":
            self.game_status = "quit" 
        elif inputString == "lose":
            self.game_status = "lost"
    def tick(self):
        pass
    def render_ending(self):
        if self.game_status == "won":
            return "You Won!"
        elif self.game_status == "lost":
            return "You Lost!"
        elif self.game_status == "quit":
            return "You Quit!"
    def render_start(self):
        title = "A Computer Science Catastrophe\n by Connor Daniel"
        return title

# Command Paths to give to the unit tester
WIN_PATH = ["win"]
LOSE_PATH = ["lose"]

def main():
    '''
    This is the Main game function. When executed, it begins a run of the game.
    Read over it to understand the engine that you are using and the order
    that the methods are executed in.
    '''
    world = World()
    print(world.render_start())
    while not world.is_done():
        if not world.is_good():
            raise ValueError("The world is in an invalid state.", world)
        print(world.render())
        is_input_good = False
        while not is_input_good:
            user_input = input("")
            is_input_good = world.is_input_good(user_input)
        world.process(user_input)
        world.tick()
    print(world.render_ending())

# Executes the main function only if this file is being run directly.
# This prevents the autograder from being confused. Never call main outside
# of this IF statement!
if __name__ == "__main__":
    ## You might comment out the main function and call each function
    ## one at a time below to try them out yourself
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # world = World()
    # world.is_done()
    # print(world.render())
    # ...
