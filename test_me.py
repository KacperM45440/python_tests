import sys

class TargetClass:
    def add_values(self, x, y):
        return x+y
    def subtract_values(self, x, y):
        return x-y
    def multiply_values(self, x, y):
        return x * y
    def divide_values(self, x, y):
        return x / y
    def divisible_by_two(self, x):
        return x % 2 == 0

def main():
    from PyQt6.QtWidgets import QApplication, QLabel, QWidget
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Test test app for testing")
    window.setGeometry(100, 100, 600, 80)
    helloMsg = QLabel("<h1>Your program didn't crash. Congratulations!</h1>", parent=window)
    helloMsg.move(45, 15)

    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    print("Program initialized.")
    main()
