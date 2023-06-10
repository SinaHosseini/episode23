import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open_File.triggered.connect(self.open_file)

        self.line_edits = [[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(
                    partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

        self.ui.actionDark_mode.triggered.connect(
            partial(self.dark_mode, i, j, self.line_edits))
        self.ui.actionLight_mode.triggered.connect(
            partial(self.light_mode, i, j, self.line_edits))

        self.new_game()

    def new_game(self):
        global puzzle
        puzzle = Sudoku(3, seed=random.randint(0, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] != None:
                    self.line_edits[i][j].setStyleSheet(
                        "QLineEdit { border-radius: 0px; border: 1px solid gray; }")
                    self.line_edits[i][j].setAlignment(
                        Qt.AlignmentFlag.AlignCenter)
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setStyleSheet(
                        "QLineEdit { border-radius: 0px; border: 1px solid gray; }")
                    self.line_edits[i][j].setAlignment(
                        Qt.AlignmentFlag.AlignCenter)
                    self.line_edits[i][j].setText("")

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open file...")[0]
        f = open(file_path, "r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for row in rows:
            cells = row[i].split(" ")
            for j in range(len(cells[j])):
                puzzle_board[i][j] = int(cells[j])

    def check(self):
        for i in range(0, 9):
            for j in range(0, 9):
                number1 = self.line_edits[i][0].text()
                number2 = self.line_edits[i][j].text()
                if number1 == number2:
                    ...
                    return False

    def validation(self, i, j, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        self.check()

    def dark_mode(self, i, j, cell):
        if self.ui.actionDark_mode.triggered:
            self.ui.centralwidget.setStyleSheet(
                "background-color: rgb(30, 30, 30);")
            for i in range(9):
                for j in range(9):
                    cell[i][j].setStyleSheet(
                        "background-color: rgb(70, 70, 70); \
                        color: rgb(255, 255, 255);")

    def light_mode(self, i, j, cell):
        if self.ui.actionLight_mode.triggered:
            self.ui.centralwidget.setStyleSheet(
                "background-color: rgb(240, 240, 240);")
            for i in range(9):
                for j in range(9):
                    cell[i][j].setStyleSheet(
                        "background-color: rgb(255, 255, 255); \
                        color: rgb(0, 0, 0);")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
