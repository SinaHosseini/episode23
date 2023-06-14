import sys
import random
import qdarktheme
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
from PySide6.QtGui import *
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open_File.triggered.connect(self.open_file)
        self.ui.actionSolve_game.triggered.connect(self.solve_game)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.action_Help.triggered.connect(self.help)
        self.ui.actionExit.triggered.connect(self.exit)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.editable_cells = []
        self.picking_boxes()
        self.checkable = True
        self.ui.actionDark_mode.triggered.connect(
            partial(self.set_color, "black"))
        self.ui.actionLight_mode.triggered.connect(
            partial(self.set_color, "light", "black"))

        self.new_game()

    def new_game(self):
        self.checkable = False
        self.editable_cells.clear()
        self.puzzle = Sudoku(3, seed=random.randint(0, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setStyleSheet("color: black;")
                if self.puzzle.board[i][j] != None:
                    self.editable_cells.append([i, j])
                    self.line_edits[i][j].setText(str(self.puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")
        self.checkable = True

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open file...")[0]
            self.editable_cells.clear()
            f = open(file_path, "r")
            big_text = f.read()
            rows = big_text.split("\n")
            puzzle_board = [[None for i in range(9)] for j in range(9)]
            for i in range(len(rows)):
                cells = rows[i].split(" ")
                for j in range(len(cells[j])):
                    puzzle_board[i][j] = int(cells[j])

            self.checkable = False
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setReadOnly(False)
                    if puzzle_board[i][j] != 0:
                        self.editable_cells.append([i, j])
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                        self.puzzle.board[i][j] = puzzle_board[i][j]
                    else:
                        self.line_edits[i][j].setText('')
                        self.line_edits[i][j].setReadOnly(False)
                        self.puzzle.board[i][j] = None
            self.checkable = True
        except:
            msg_box = QMessageBox()
            msg_box.setText("An exception occurred to load the file")
            msg_box.exec()

    def false_cells(self, row, col):
        if [row, col] in self.editable_cells:
            self.line_edits[row][col].setStyleSheet("background-color: pink;")
        else:
            self.line_edits[row][col].setStyleSheet("background-color: red;")

    def check(self, i=-1, j=-1):
        output = True
        self.setStyleSheet("")
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setStyleSheet("")

        for row in range(9):
            for col in range(9):
                number1 = self.line_edits[row][col].text()
                if number1 == "":
                    output = False
                elif [row, col] not in self.editable_cells:
                    self.line_edits[row][col].setStyleSheet(
                        "color: yellow;")
                for row9 in range(row+1, 9):
                    number2 = self.line_edits[row9][col].text()
                    if number1 == number2 and number2 != "":
                        self.false_cells(row, col)
                        self.false_cells(row9, col)
                        output = False

                for col9 in range(col+1, 9):
                    number2 = self.line_edits[row][col9].text()
                    if number1 == number2 and number2 != "":
                        self.false_cells(row, col)
                        self.false_cells(row, col9)
                        output = False

        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                for row in range(n, n+3):
                    for col in range(m, m+3):
                        number1 = self.line_edits[row][col].text()
                        for row3 in range(n, n+3):
                            for col3 in range(m, m+3):
                                number2 = self.line_edits[row3][col3].text()
                                if number1 == number2 and number2 != "" and not (row == row3 and col == col3):
                                    self.false_cells(row, col)
                                    self.false_cells(row3, col3)
                                    output = False

        return output

    def validation(self, i, j, text):
        if self.checkable:
            if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self.line_edits[i][j].setText("")

        if self.check(i, j):
            msg_box = QMessageBox()
            msg_box.setText("YOU WIN 🎊")
            msg_box.setWindowTitle("WIN")
            msg_box.exec()

    def picking_boxes(self):
        global i, j
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(QtCore.Qt.AlignCenter)
                new_cell.setSizePolicy(
                    QSizePolicy.Expanding, QSizePolicy.Expanding)
                new_cell.setMinimumWidth(30)
                new_cell.setFont(QFont("Center", pointSize=15))
                new_cell.setStyleSheet("color: black;")
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def solve_game(self):
        self.checkable = False
        for i in range(9):
            for j in range(9):
                if self.puzzle.board[i][j] is None:
                    self.line_edits[i][j].setText(
                        str(self.puzzle.solve().board[i][j]))
                    self.line_edits[i][j].setStyleSheet("color: green;")

        self.checkable = True

    def about(self):
        msg_box = QMessageBox()
        msg_box.setText("Sudoku is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 * 9 grid with digits so that each column, each row, and each of the nine 3 * 3 subgrades that compose the grid (also called 'boxes', 'blocks', or 'regions') contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.\n\nFrench newspapers featured variations of the Sudoku puzzles in the 19th century, and the puzzle has appeared since 1979 in puzzle books under the name Number Place. However, the modern Sudoku only began to gain widespread popularity in 1986 when it was published by the Japanese puzzle company Nikoli under the name Sudoku, meaning 'single number'.It first appeared in a U.S. newspaper, and then The Times (London), in 2004, thanks to the efforts of Wayne Gould, who devised a computer program to rapidly produce unique puzzles.")
        msg_box.exec()

    def help(self):
        msg_box = QMessageBox()
        msg_box.setText("The rules for sudoku are simple. A 9*9 square must be filled in with numbers from 1-9 with no repeated numbers in each line, horizontally or vertically. To challenge you more, there are 3*3 squares marked out in the grid, and each of these squares can't have any repeat numbers either.")
        msg_box.exec()

    def set_color(self, color, textColor='black'):
        if color == "black":
            qdarktheme.setup_theme("dark")
        else:
            qdarktheme.setup_theme("light")

        self.check()

    def exit(self):
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
