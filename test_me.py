import sys
import math
from collections import defaultdict
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QCursor

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
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 + (self.z - other_point.z) ** 2)
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
class Plane:
    def __init__(self, a=None, b=None, c=None, d=None, point=None, vector=None, p1=None, p2=None, p3=None):
        if a is not None and b is not None and c is not None and d is not None:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
        elif point and vector:
            self.a = vector.x
            self.b = vector.y
            self.c = vector.z
            self.d = -(self.a * point.x + self.b * point.y + self.c * point.z)
        elif p1 and p2 and p3:
            v1 = Vector3D(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)
            v2 = Vector3D(p3.x - p1.x, p3.y - p1.y, p3.z - p1.z)
            normal_vector = v1.multiply_vectors(v2)
            self.a = normal_vector.x
            self.b = normal_vector.y
            self.c = normal_vector.z
            self.d = -(self.a * p1.x + self.b * p1.y + self.c * p1.z)
        else:
            raise ValueError("Can't create a plane from given arguments.")

    def distance_to_point(self, point):
        numerator = abs(self.a * point.x + self.b * point.y + self.c * point.z + self.d)
        denominator = math.sqrt(self.a**2 + self.b**2 + self.c**2)
        return numerator / denominator
    
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Computer Info Box")

    window.move(500, 200)
    window.setStyleSheet(
        "background-color: #CEDEFF;"
    )
    grid = QGridLayout()

    ### Text box
    groupBoxText = QGroupBox("Output")
    groupBoxText.setStyleSheet(
                     'QGroupBox {'
                     'border: 1px solid #F75A85;'
                     'margin-top: 10px; }'
                     
                     'QGroupBox:title {'
                     'subcontrol-origin: margin;'
                     'subcontrol-position: top center;'
                     'padding-left: 7px;'
                     'padding-right: 7px; }'
                     )
    textEdit = QTextEdit()
    textEdit.setStyleSheet(
                    'QTextEdit {'
                    'border: 0;}'
                    )
    textEdit.setReadOnly(True)
    groupText = QVBoxLayout()
    groupText.addWidget(textEdit)
    groupBoxText.setLayout(groupText)

    ### Button box
    groupBoxButtons = QGroupBox("Actions")
    groupBoxButtons.setStyleSheet(
                     'QGroupBox {'
                     'border: 1px solid #F75A85;'
                     'margin-top: 10px; }'
                     
                     'QGroupBox:title {'
                     'subcontrol-origin: margin;'
                     'subcontrol-position: top center;'
                     'padding-left: 7px;'
                     'padding-right: 7px; }'
                     )
    pushButton1 = QPushButton("IPv4")
    pushButton2 = QPushButton("Proxy")
    pushButton3 = QPushButton("OS + Hardware")
    pushButton4 = QPushButton("BIOS version")
    pushButton5 = QPushButton("Hostname")

    groupButtons = QVBoxLayout()
    groupButtons.addWidget(pushButton1)
    groupButtons.addWidget(pushButton2)
    groupButtons.addWidget(pushButton3)
    groupButtons.addWidget(pushButton4)
    groupButtons.addWidget(pushButton5)
    groupBoxButtons.setLayout(groupButtons)

    ### Set layout
    table = QTableWidget()
    table.setRowCount(3)
    table.setColumnCount(3)
    grid.addWidget(groupBoxButtons, 1, 1)
    grid.addWidget(groupBoxText, 1, 0)

    window.show()
    window.setLayout(grid)
    sys.exit(app.exec())
    
if __name__ == "__main__":
    print("Program initialized.")
    main()
