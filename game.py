from player import HumanPlayer, RandomComputerPlayer



class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3 x 3 board 
        self.current_winner = None # keep track of winner 
        
    def print_board(self):
        # this is just getting the rows 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # this is saying which group of three spaces are we choosing the first one the second one or the third 
            print('|' + '|'.join(row) + '|')
    
    @staticmethod # this is a static method because it does not relate to any specific board 
    def print_board_nums():
        # 0 | 1 | 2 ect (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range (j*3, (j+1) *3)] for j in range(3)]
        # give me what indices are in the rows for each of the rows 
        for row in number_board:
            print('|' + '|'.join(row) + '|')
            
            
    def available_moves(self): # what are the avaliable moves after you make a move 
        #return [] # this list will be a list of indices 
        return [i for i, spot in enumerate(self.board) if spot == ' ']



    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ') # number of spaces in the board 

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true, if invalid, return false 
        if self.board[square] == ' ': # if there is nothing there 
            self.board[square] = letter    # then we assign that letter to that square 
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these. 
        #first lets check the row 
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check colum 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
              return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
              return True
        return False

            

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums
        
    letter = 'X' #starting letter 
    # iterate while the game still has empty squares 
    # (we don't have to worry about winner because well just return the which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player 
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
            
        # lets define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board() # once we assign it to the square we need to rerender the board
                print('')  #just empty line 
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            #after we made our move, we need to alternate letters 
            letter = 'O' if letter == 'X' else 'X' #switches players 
        
    if print:
        print('It is a tie!')
            
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)