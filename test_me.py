import sys
import pytest

#Classes that hold tests must be named starting with Test
#Any file that is to contain tests must be named starting with test_
#Any function in a file that should be treated as a test must also start with test_
#
#my_object.method("foo") == MyClass.method(my_object, "foo")

class TestClass:
    def divisible_by_two(self, x):
        return x % 2 == 0

    @pytest.mark.parametrize("givenNumber, expectedOutcome", [(1, False), (2, True), (3, False),(4, False)])
    def test_capping(self, givenNumber, expectedOutcome):
        assert self.divisible_by_two(givenNumber) == expectedOutcome

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
