from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy
import tictactoe
from minimax import MiniMax
import sys

# Create window class
class Window(QMainWindow):
    #constructor
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Tic Tac Toe by Jason Carter")

        # setting geometry
        self.setGeometry(100, 100, 300, 500)

        # calliing method
        self.UiComponents()

        # Showing all the widgets
        self.show()

        # Initalize game
        self.game = tictactoe.TicTacToe()

    def UiComponents(self):
        # Create a push button list
        self.push_list = []

        # creating 2d list of push buttons
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            # adding 3 push button in single row
            self.push_list.append(temp)

        # x and y coord
        x = 90
        y = 80

        # traversing through the push button list
        for i in range(3):
            for j in range(3):

                # setting geometry to the button
                self.push_list[i][j].setGeometry(x*i + 20, y*j + 20, 80, 80)

                # setting font to the button
                self.push_list[i][j].setFont(QFont(QFont('Times', 17)))

                # adding action to the button
                self.push_list[i][j].clicked.connect(self.action_called)

        # creating label to display who wins
        self.label = QLabel(self)

        # setting geomoetry to the label
        self.label.setGeometry(20, 300, 260, 60)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 2px solid black;"
                                 "background : white;"
                                 "}")
        
        # setting label alignment
        self.label.setAlignment(Qt.AlignCenter)

        # setting font to the label
        self.label.setFont(QFont('Times', 15))

        # creating push button to restart the score
        reset_game = QPushButton("Reset-Game", self)

        # Setting geometry
        reset_game.setGeometry(50, 380, 200, 50)

        # adding action to reset the push button
        reset_game.clicked.connect(self.reset_game_action)

    # method called by reset button
    def reset_game_action(self):

        # reinitalize game to reset 
        self.game = tictactoe.TicTacToe()

        # making label text empty
        self.label.setText("")

        # traverse push list
        for buttons in self.push_list:
            for button in buttons:
                # making all the button enabled
                button.setEnabled(True)
                # removing text of all the buttons
                button.setText("")
    
    # action called by the push buttons
    def action_called(self):

        # get the button that called the action
        button = self.sender()

        # disable button
        button.setEnabled(False)

        # traverse through the buttons to get the coords of button (there is probably a better way to do this)
        for i in range(len(self.push_list)):
            for j in range(len(self.push_list)):
                if button == self.push_list[i][j]:
                    move = (i, j)
                    break
        
        # set the text of the button to X
        button.setText("X")
        # make the move in the game
        self.game.make_move(self.game.get_X_player(), move)

        # if the game is unfinished, make the AI move
        if self.game.get_status() == "UNFINISHED":
            game_object = copy.deepcopy(self.game)
            ai = MiniMax(game_object)
            ai_move = ai.minimax(game_object)
            button = self.push_list[ai_move[0]][ai_move[1]]
            button.setText("O")
            button.setEnabled(False)
            self.game.make_move(self.game.get_O_player(), ai_move)
        
        # determine if there is a win or draw
        win = self.game.get_status()

        # set the game status label to empty text
        text = ""

        if win == "X_WON":
            text = "X WON"
        if win == "O_WON":
            text = "O WON"
        if win == "DRAW":
            text = "DRAW"

        self.label.setText(text)

app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec())