import sys
import math
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
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
class Line:
    def __init__(self, a=None, b=None, c=None, p1=None, p2=None, point=None, vector=None):
        if a is not None and b is not None and c is not None:
            self.a = a
            self.b = b
            self.c = c
        elif p1 and p2:
            self.a = p2.y - p1.y
            self.b = p1.x - p2.x
            self.c = -self.a * p1.x - self.b * p1.y
        elif point and vector:
            self.a = vector.y
            self.b = -vector.x
            self.c = -self.a * point.x - self.b * point.y
        else:
            raise ValueError("Can't create a straight line from given arguments.")

    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        return (math.isclose(self.a * other.b, self.b * other.a) and
                math.isclose(self.b * other.c, self.c * other.b) and
                math.isclose(self.a * other.c, self.c * other.a))
class Vector:
    def __init__(self, x=None, y=None, p1=None, p2=None, line=None):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif p1 and p2:
            self.x = p2.x - p1.x
            self.y = p2.y - p1.y
        elif line:
            self.x = -line.b
            self.y = line.a
        else:
            raise ValueError("Can't create a vector from given arguments.")

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def multiply_vectors(self, other):
        z = self.x * other.y - self.y * other.x
        return Vector3D(0, 0, z)

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

class Vector3D(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y) and math.isclose(self.z, other.z)
    
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
