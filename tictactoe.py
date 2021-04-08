# Description:  A class containing the tic tac toe game

class TicTacToe:
    """A tic tac toe game that also stores the game board and the players"""

    def __init__(self, player_x="X", player_o="O", board_size=3):
        """Instantiate the game as an object and initialize the game."""
        self.board_size = board_size
        self._board = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        self._player_x = player_x
        self._player_o = player_o
        self._game_status = "UNFINISHED"

    def get_current_player(self):
        """Return the next player based on the the board itself."""
        # calculating the current count of X' and O's on the board
        x_count = 0
        o_count = 0
        for row in self._board:
            for cell in row:
                if cell == "X":
                    x_count += 1
                elif cell == "O":
                    o_count += 1
        # return the next player based off the count of X's and O's
        if x_count <= o_count:
            return self._player_x
        else:
            return self._player_o

    def get_board_size(self):
        return self.board_size
        
    # Add return X and O player for minimax
    def get_X_player(self):
        return self._player_x
    
    def get_O_player(self):
        return self._player_o
        
    def get_board(self):
        """Return the current game board."""
        return self._board

    def return_status(self):
        """Returns the current game status."""
        return self._game_status

    def check_winner(self):
        """use get_current_player to determine if X_Won or O_Won"""
        if self.get_current_player() == self._player_o:
            self._game_status = "X_WON"
        else:
            self._game_status = "O_WON"

    def get_status(self):
        """Takes the current game board and determines the game status."""
        #   Win Check - rows of self._board
        for row in self._board:
            if len(set(row)) == 1 and None not in row:
                self.check_winner()
                return self._game_status

        #   Transpose the rows and columns of self._board.
        transposed_board = list(map(list, zip(*self._board)))

        #   Win Check - rows of transposed_board (aka columns of self._board)
        for row in transposed_board:
            if len(set(row)) == 1 and None not in row:
                self.check_winner()
                return self._game_status

        #   Win Check - diagonal of self._board (upper left to lower right)
        if self._board[self.board_size // 2][self.board_size // 2] is not None:
            if len(set([self._board[i][i] for i in range(self.board_size)])) == 1:
                self.check_winner()
                return self._game_status

        #   Win Check - diagonal of self._board (lower left to upper right)
            elif len(set([self._board[i][self.board_size - i - 1] for i in range(self.board_size)])) == 1:
                self.check_winner()
                return self._game_status

        #   Draw Check
        if self.get_possible_move() == set():
            self._game_status = "DRAW"
            return self._game_status

        return self._game_status

    def get_possible_move(self):
        """Returns a list of move (2-tuples) of all possible moves."""
        moves = set()
        for i, r in enumerate(self._board):
            for j, c in enumerate(r):
                if c is None:
                    moves.add((i, j))
        return moves

    def print_board(self):
        """Print out the current game board and next player's turn."""
        for row in range(0, self.board_size):
            for col in range(0, self.board_size):
                if self._board[row][col] is None:
                    print(row, col, end = '')
                else:
                    print(chr(32),self._board[row][col], chr(32), sep='', end = '')
                
                if col != self.board_size-1:
                    print("|", end = '')
            print()
            if row != self.board_size-1:
                for i in range(self.board_size-1):
                    print(chr(32)*2, '|', end = '')

                print()

        print()

    def make_move(self, player, move):
        """Takes player ('X' or 'O') and the move (as a 2-tuple) as input,
        determine if the move is valid, and make the move on the board.
        Lastly, update game status.
        """

        # Validate if the player's name is one of the player.
        if player != self._player_x and player != self._player_o:
            raise IncorrectPlayerNameError

        # Validate if it is this player's turn
        if player != self.get_current_player():
            raise IncorrectPlayerTurnError

        # Is the move in the list of all possible move?
        if move not in self.get_possible_move():
            raise IncorrectMoveError

        # Update the board using the player and the move.
        self._board[move[0]][move[1]] = 'X' if player == self._player_x else 'O'

        # Update and return the status of the game (Pending implementation of get_status method)
        return self.get_status()


class IncorrectPlayerNameError(Exception):
    """Raised when the entered name does not match any of the player's name."""
    pass


class IncorrectPlayerTurnError(Exception):
    """Raised when the entered name is one of the player but it is not his/her turn."""
    pass


class IncorrectMoveError(Exception):
    """Raised when the entered move is not one of the possible move."""
    pass
