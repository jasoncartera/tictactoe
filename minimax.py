import math
import copy
from random import *

class MiniMax:
    # Utility function to determine if a game is over or not
    def __init__(self, game_object):
        """Initalizes MiniMax Ai for tic-tac-toe"""
        self._game_copy = copy.deepcopy(game_object)

    def terminal(self, game_object):
        """
        Returns True if game is over, False otherwise.
        """
        if self._game_copy.get_status() != "UNFINISHED" or not self._game_copy.get_possible_move():
            return True
        else:
            return False

    # Utility function to provide numerical output for a game outcome.
    def utility(self, game_object):
        """
        Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
        """
        if self._game_copy.return_status() == "X_WON":
            return 1
        elif self._game_copy.return_status() == "O_WON":
            return -1
        else:
            return 0

    def recopy_game(self, game_object):
        self._game_copy = copy.deepcopy(game_object)
        return self._game_copy

    # Minimax function determines the optimal move for a given game state. 
    # The game state is passed as a deep copy of the object in play in console.
    def minimax(self, game_object):
        """
        Returns the optimal action for the current player on the board.
        Input is a copy of the board from console.py
        """

        if self.terminal(game_object):
            return None
        
        # Optimize if player chooses O and first move is computer
        if len(game_object.get_possible_move()) == (game_object.board_size*game_object.board_size):
            i = randint(0,2)
            j = randint(0,2)
            return (i,j)

        if game_object.get_current_player() == game_object.get_X_player():
            best_v = -math.inf
            for action in game_object.get_possible_move():
                # For every action make a move then pass the move to min_value
                game_copy = self.recopy_game(game_object)
                game_copy.make_move(game_copy.get_current_player(), action)
                board = game_copy.get_board()
                max_v = self.min_value(game_copy, board)
                if max_v > best_v:
                    best_v = max_v
                    best_move = action

        if game_object.get_current_player() == game_object.get_O_player():
            best_v = math.inf
            for action in game_object.get_possible_move():
                game_copy = self.recopy_game(game_object)
                game_copy.make_move(game_copy.get_current_player(), action)
                board = game_copy.get_board()
                min_v = self.max_value(game_copy, board)
                if min_v < best_v:
                    best_v = min_v
                    best_move = action
                    
        return best_move    
        

    def max_value(self, game_object, board):
        """Minimizing player will emulate the maximizing player by finding the maximum game utility using this function"""
        v = -math.inf
        if self.terminal(game_object):
            return self.utility(game_object)
        for action in game_object.get_possible_move():
            game_copy = self.recopy_game(game_object)
            game_copy.make_move(game_copy.get_current_player(), action)
            board = game_copy.get_board()
            v = max(v, self.min_value(game_copy, board))
        return v

    def min_value(self, game_object, board):
        """Maximimizing player will emulate minimizing player with this function and return the best uitlity value"""
        v = math.inf
        if self.terminal(game_object):
            return self.utility(game_object)
        for action in game_object.get_possible_move():
            game_copy = self.recopy_game(game_object)
            game_copy.make_move(game_copy.get_current_player(), action)
            board = game_copy.get_board()
            v = min(v, self.max_value(game_copy, board))
        return v