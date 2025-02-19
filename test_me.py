import os
import re
import sys
import math
import subprocess
import platform
import socket
import requests
import multiprocessing
import psutil
import pytest

from urllib import request
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
    

class Buttons:
    def button1_action(window):
        process = QProcess()  
        process.start("cmd", ["/c", "ipconfig", "/all"])
        process.waitForFinished()
        output = process.readAllStandardOutput().data().decode('windows-1252')

        ip_string = ">>>IP Configuration\n"
        window.textEdit.append(ip_string)
        print(ip_string)

        data_array = []
        
        match = re.search(r"(Description.*?:.*)", output)
        if match:
            description = match.group(1)
            window.textEdit.append(description)
            print(description)
            data_array.append(description.strip())
        match = re.search(r"(DHCP Enabled.*?:.*)", output)
        if match:
            dhcp = match.group(1)
            window.textEdit.append(dhcp)
            print(dhcp)
            data_array.append(dhcp.strip())
        match = re.search(r"(IPv4 Address.*?:.*)", output)
        if match:
            address = match.group(1)
            window.textEdit.append(address)
            print(address)
            data_array.append(address.strip())

        return data_array
        
    def button2_action(window):
        proxy_string = ">>>Proxy Configuration\n"
        window.textEdit.append(proxy_string)
        print(proxy_string)

        data_array = []
        
        proxies = requests.utils.get_environ_proxies("http://example.com")
        if proxies:
            for protocol, proxy in proxies.items():
                try:
                    response = requests.get("http://ipinfo.io/json", proxies={protocol: proxy}, timeout=5)
                    if response.status_code == 200:
                        response1_string = f"Proxy is active: {proxy}\n"
                        response2_string = "Proxy's public IP and port:", proxy + "\n"
                        window.textEdit.append(response1_string)
                        window.textEdit.append(response2_string)
                        print(response1_string)
                        print(response2_string)
                        data_array.append(response1_string.strip())
                        data_array.append(response2_string.strip())
                except Exception as e:
                    exception_string = f"Failed to connect using proxy {proxy}: {e}\n"
                    window.textEdit.append(exception_string)
                    print(exception_string)
                    data_array.append(exception_string.strip())
        else:
            noproxy_string = "No proxy detected.\n"
            window.textEdit.append("No proxy detected.\n")
            print("No proxy detected.\n")
            data_array.append(noproxy_string.strip())

        return data_array        

    def button3_action(window):
        system = platform.system()
        version = platform.version()
        processor = str(os.cpu_count())
        memory = str(round(psutil.virtual_memory().total/(1024.**3)))

        data_array = []
        
        hardware_string = ">>>Hardware Configuration\n"
        system_string = "System version: " + system + " " + version + "\n"
        cpu_string = "CPU cores: "+ processor + "\n"
        ram_string = "Total RAM: "+ memory + "GB\n"
        window.textEdit.append(hardware_string)
        window.textEdit.append(system_string)
        window.textEdit.append(cpu_string)
        window.textEdit.append(ram_string)
        print(hardware_string)
        print(system_string)
        print(cpu_string)
        print(ram_string)
        data_array.append(system_string.strip())
        data_array.append(cpu_string.strip())
        data_array.append(ram_string.strip())

        return data_array

    def button4_action(window):
        bios_string = ">>>BIOS Version\n"
        window.textEdit.append(bios_string)
        print(bios_string)

        data_array = []
        
        if sys.platform == 'win32':            
            process = QProcess()  
            process.start("systeminfo.exe")
            process.waitForFinished()
            output = process.readAllStandardOutput().data().decode('windows-1252')
            match = re.search(r"(BIOS Version:*?:.*)", output)
            if match:
                version = match.group(1).strip()
                version_string = version + "\n"
                window.textEdit.append(version_string)
                print(version_string)
                data_array.append(version_string.strip())
        else:
            process = QProcess()  
            process.start("dmidecode --string bios-version", universal_newlines=True, shell=True) #untested
            process.waitForFinished()
            output = process.readAllStandardOutput().data().decode('utf-8')
            output_string = output + "\n"
            window.textEdit.append(output_string)
            print(output_string)
            data_array.append(output_string.strip())

        return data_array
        
    def button5_action(window):
        hostname_string = ">>>Hostname\n"
        socket_string = socket.gethostname() + "\n"

        data_array = []
        
        window.textEdit.append(hostname_string)
        window.textEdit.append(socket_string)
        print(hostname_string)
        print(socket_string)
        data_array.append(socket_string.strip())

        return data_array

def set_window_properties(window):
    window.setWindowTitle("Computer Info Box")
    window.setGeometry(10, 10, 640, 512)
    window.move(500, 200)
    window.setStyleSheet(
        "background-color: #CEDEFF;"
    )

def set_textbox_properties(groupBoxText, groupText, window):
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
     
    window.textEdit.setStyleSheet(
                    'QTextEdit {'
                    'border: 0;}'
                    )
    window.textEdit.setReadOnly(True)
    groupText.addWidget(window.textEdit)
    groupBoxText.setLayout(groupText)

def set_button_properties(groupBoxButtons, groupButtons, window):
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
    pushButton1.pressed.connect(lambda: Buttons.button1_action(window))
    pushButton2 = QPushButton("Proxy")
    pushButton2.pressed.connect(lambda: Buttons.button2_action(window))
    pushButton3 = QPushButton("OS + Hardware")
    pushButton3.pressed.connect(lambda: Buttons.button3_action(window))
    pushButton4 = QPushButton("BIOS version")
    pushButton4.pressed.connect(lambda: Buttons.button4_action(window))
    pushButton5 = QPushButton("Hostname")
    pushButton5.pressed.connect(lambda: Buttons.button5_action(window))
    
    groupButtons.addWidget(pushButton1)
    groupButtons.addWidget(pushButton2)
    groupButtons.addWidget(pushButton3)
    groupButtons.addWidget(pushButton4)
    groupButtons.addWidget(pushButton5)
    groupBoxButtons.setLayout(groupButtons)

def set_layout_properties(groupBoxButtons, groupBoxText, table, grid, window):
    table.setRowCount(3)
    table.setColumnCount(3)
    grid.addWidget(groupBoxButtons, 1, 1)
    grid.addWidget(groupBoxText, 1, 0)
    window.show()
    window.setLayout(grid)

def check_connection():
    try:
        request.urlopen('https://8.8.4.4', timeout=1)
        return True
    except request.URLError as err: 
        return False

def test_window():
    app, window = main(True)
    assert True == check_connection()
    assert 640 == window.size().width()
    assert 512 == window.size().height()
    assert '#cedeff' == window.palette().window().color().name()
    assert 'Segoe UI' == window.textEdit.font().family()
#    assert 'Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #3' == Buttons.button1_action(window)[0] #Laptop
    assert 'Description . . . . . . . . . . . : Intel(R) Ethernet Controller (3) I225-V #2' == Buttons.button1_action(window)[0] #Komputer
    assert 'DHCP Enabled. . . . . . . . . . . : Yes' == Buttons.button1_action(window)[1]
    assert 'No proxy detected.' == Buttons.button2_action(window)[0]
    assert ['System version: Windows 10.0.19045', 'CPU cores: 20', 'Total RAM: 32GB'] == Buttons.button3_action(window) #Komputer
    assert 'BIOS Version:              American Megatrends International, LLC. A.J0, 15.08.2024' == Buttons.button4_action(window)[0] #Komputer
    assert 'DESKTOP-9921IU8' == Buttons.button5_action(window)[0] #Komputer

def main(test):
    app = QApplication(sys.argv)
    window = QWidget()
    grid = QGridLayout()
    groupBoxText = QGroupBox("Output")
    window.textEdit = QTextEdit()
    groupText = QVBoxLayout()
    groupBoxButtons = QGroupBox("Actions")
    groupButtons = QVBoxLayout()
    table = QTableWidget()
    
    set_window_properties(window)
    set_textbox_properties(groupBoxText, groupText, window)
    set_button_properties(groupBoxButtons, groupButtons, window)
    set_layout_properties(groupBoxButtons, groupBoxText, table, grid, window)  
    
    sys._excepthook = sys.excepthook 
    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback) 
        sys.exit(1) 
    sys.excepthook = exception_hook

    if test:
        return app, window

    sys.exit(app.exec())

def command_line_args(args):
    app = QApplication(sys.argv)
    window = QWidget()
    window.textEdit = QTextEdit()
    for arg in args:
        if arg == '-button1':
            Buttons.button1_action(window)
        if arg == '-button2':
            Buttons.button2_action(window)
        if arg == '-button3':
            Buttons.button3_action(window)
        if arg == '-button4':
            Buttons.button4_action(window)
        if arg == '-button5':
            Buttons.button5_action(window)
        if arg == 'help' or arg == '-help' or arg == '/help':
            print("Available commands (you can use multiple):")
            print("-button1 | See IPv4 configuration of computer")
            print("-button2 | Check availability of proxy")
            print("-button3 | See computer configuration")
            print("-button4 | Check BIOS version")
            print("-button5 | See computer name")    
                  
if __name__ == "__main__":
    print("Program initialized.")
    if len(sys.argv) > 1:
        command_line_args(sys.argv)
        sys.exit()   
    main(False)
    
