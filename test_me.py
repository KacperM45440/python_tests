import sys
from collections import defaultdict

class TargetClass:
    def add_values(self, x, y):
        return x+y
    def subtract_values(self, x, y):
        return x-y
    def multiply_values(self, x, y):
        return x * y
    def divide_values(self, x, y):
        if y == 0:
            raise ValueError("division by zero")
        return x / y
    def divisible_by_two(self, x):
        return x % 2 == 0
    def fibonacci_iterative(self, n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    def fibonacci_recursive(self, n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)
    def factorial_iterative(self, n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    def factorial_recursive(self, n):
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial_recursive(n - 1)
    def euklides_iterative(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("a and b must both be non-negative integers")
        while b:
            a, b = b, a % b
        return a
    def euklides_recursive(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("a and b must both be non-negative integers")
        if b == 0:
            return a
        return self.euklides_recursive(b, a % b)
    def sort_files(self, files_string):
        if not files_string.strip():
            return files_string
        
        files = files_string.split(", ")
        ext_dict = defaultdict(list)
        
        for file in files:
            if "." not in file:
                continue
            name, ext = file.rsplit(".", 1)
            ext_dict[ext.lower()].append(file)
        sorted_ext = sorted(ext_dict.keys(), key=lambda x: (-len(ext_dict[x]), x))
        sorted_files = [file for ext in sorted_ext for file in sorted(ext_dict[ext], key=str.lower)]
        return ", ".join(sorted_files)
    
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
