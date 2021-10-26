import math
import random


# we need a based player class and we are going to initialize it with the letter the player is going to represent 
class Player:
    def __init__(self, letter):
        # either x or o
        self.letter = letter
        
    # we want all players to get their next move 
    def get_move(self, game):
    # we will build on this base player for the human and ai players using inheritence 
        pass  # in python pass is a null statment that does nothing, it is used to create loops if else statement functions and classes with an empty body
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)   # inheritance allows us to inherit attributes and methods from a parent class to child classes. 
        # as part of our initialization we have to init the super class
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square # get a random valid spot for our next move 
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game): # human player needs to choose their spot through a terminal 
        valid_square = False #they have not put anything in yet 
        val = None # dito the above line 
        while not valid_square: 
            square = input(self.letter + '\s turn. Input move (0-9): ') 
            # were going to check that this is a correct value by trying to cast 
            # it to an integer, and if it's not, then we say its invalid 
            # if that spot is not avilable on the board, we also say its invalid 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again')
        return val
        

        