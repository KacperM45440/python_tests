import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QHBoxLayout, QWidget, QLabel
from PyQt6.QtCore import QTimer, Qt, QSize
from functools import partial

class GameLogic:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.mines = set()
        self.flags = set()
        self.question_marks = set()

    def generate_mines(self, first_row, first_col):
        self.mines.clear()
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != (first_row, first_col):
                self.mines.add((row, col))

    def count_adjacent_mines(self, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        return sum((row + dr, col + dc) in self.mines for dr, dc in directions if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols)

    def toggle_flag(self, row, col):
        if (row, col) in self.flags:
            self.flags.remove((row, col))
            self.question_marks.add((row, col))
            return "?"
        elif (row, col) in self.question_marks:
            self.question_marks.remove((row, col))
            return ""
        elif len(self.flags) < self.num_mines:
            self.flags.add((row, col))
            return "F"
        return None

class Timer(QTimer):
    def __init__(self, update_callback):
        super().__init__()
        self.time = 0
        self.update_callback = update_callback
        self.timeout.connect(self.update_time)

    def update_time(self):
        self.time += 1
        self.update_callback(self.time)

    def reset(self):
        self.time = 0
        self.stop()

class Minesweeper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("45440 Minesweeper")
        self.setFixedSize(400, 450)

        self.rows = 8
        self.cols = 8
        self.num_mines = 10
        self.first_click = True
        self.game_over = False
        self.logic = GameLogic(self.rows, self.cols, self.num_mines)

        self.timer = Timer(self.update_timer)
        self.buttons = {}
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        main_layout = QGridLayout()
        top_panel = QGridLayout()
        self.setStyleSheet("background-color: darkgray;")
        digital_font = "font-family: 'Courier New'; font-size: 30px; color: red; text-align: center;"

        self.mine_counter = QLabel("0"+str(self.num_mines))
        self.mine_counter.setFixedSize(50, 30)
        self.mine_counter.setStyleSheet(f"background-color: black; {digital_font}")
        self.mine_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_panel.addWidget(self.mine_counter, 1, 0)

        self.smile_button = QPushButton(":)")
        self.smile_button.setFixedSize(50, 30)
        self.smile_button.clicked.connect(self.reset_game)
        top_panel.addWidget(self.smile_button, 1, 1)

        self.time_counter = QLabel("000")
        self.time_counter.setFixedSize(50, 30)
        self.time_counter.setStyleSheet(f"background-color: black; {digital_font}")
        self.time_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_panel.addWidget(self.time_counter, 1, 2)

        top_panel.setSpacing(0)
        top_panel.setContentsMargins(0, 0, 0, 0)
        top_panel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(top_panel, 0, 0, 1, 1)

        grid_widget = QWidget()
        grid_layout = QGridLayout()

        button_style = "background-color: lightgray; padding: 0px; margin: 0px;"

        for row in range(self.rows):
            for col in range(self.cols):
                button = QPushButton()
                button.setFixedSize(QSize(50, 50))
                button.setStyleSheet(button_style)
                button.pressed.connect(partial(self.on_mouse_press, row, col))
                button.released.connect(partial(self.on_click, row, col))
                button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                button.customContextMenuRequested.connect(partial(self.toggle_flag, row, col))
                grid_layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setHorizontalSpacing(0)
        grid_widget.setLayout(grid_layout)

        main_layout.addWidget(grid_widget, 1, 0)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def update_timer(self, time):
        self.time_counter.setText(f"{time:03}")

    def on_mouse_press(self, row, col):
        if self.buttons[(row, col)].isEnabled() and not self.game_over:
            self.smile_button.setText(":O")

    def on_click(self, row, col):
        if self.game_over:
            return

        self.smile_button.setText(":)")
        if self.first_click:
            self.logic.generate_mines(row, col)
            self.timer.start(1000)
            self.first_click = False

        if (row, col) in self.logic.mines:
            self.reveal_mines()
            self.smile_button.setText(":(")
            QMessageBox.critical(self, "Game Over", "Boom! You lost.")
            self.timer.stop()
            self.game_over = True
        else:
            self.reveal_cell(row, col)
            if self.check_win():
                self.smile_button.setText(":D")
                QMessageBox.information(self, "You Win!", "Congratulations!")
                self.timer.stop()
                self.game_over = True

    def toggle_flag(self, row, col):
        if self.game_over:
            return

        button = self.buttons[(row, col)]
        result = self.logic.toggle_flag(row, col)
        if result is not None:
            button.setText(result)
            if result == "F":
                button.setStyleSheet("background-color: lightgray; color: red;")
            elif result == "?":
                button.setStyleSheet("background-color: lightgray; color: black;")
            else:
                button.setStyleSheet("background-color: lightgray;")
        self.mine_counter.setText("0" + str(self.num_mines - len(self.logic.flags)))

    def reveal_mines(self):
        for (r, c) in self.logic.mines:
            self.buttons[(r, c)].setText("*")
            self.buttons[(r, c)].setEnabled(False)

    def reveal_cell(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        button = self.buttons[(row, col)]
        if not button.isEnabled():
            return

        if (row, col) in self.logic.flags:
            self.logic.flags.remove((row, col))
            self.logic.num_mines += 1
            self.mine_counter.setText("0" + str(self.num_mines - len(self.logic.flags)))
            button.setText("")

        if (row, col) in self.logic.mines:
            button.setText("*")
            button.setEnabled(False)
            return

        button.setEnabled(False)
        mine_count = self.logic.count_adjacent_mines(row, col)
        if mine_count > 0:
            button.setText(str(mine_count))
            button.setStyleSheet(f"background-color: darkgray; color: {self.get_number_color(mine_count)};")
        else:
            button.setStyleSheet("background-color: darkgray;")
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        self.reveal_cell(row + dr, col + dc)

    def get_number_color(self, number):
        colors = {
            1: "blue",
            2: "green",
            3: "red",
            4: "purple",
            5: "brown",
            6: "cyan",
            7: "black",
            8: "gray"
        }
        return colors.get(number, "black")

    def check_win(self):
        for (r, c), button in self.buttons.items():
            if button.isEnabled() and (r, c) not in self.logic.mines:
                return False
        return True

    def reset_game(self):
        self.logic = GameLogic(self.rows, self.cols, self.num_mines)
        self.first_click = True
        self.game_over = False
        self.timer.reset()
        self.time_counter.setText("000")
        for button in self.buttons.values():
            button.setEnabled(True)
            button.setText("")
            button.setStyleSheet("background-color: lightgray;")
        self.smile_button.setText(":)")
        self.mine_counter.setText("0" + str(self.num_mines))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Minesweeper()
    game.show()
    sys.exit(app.exec())
