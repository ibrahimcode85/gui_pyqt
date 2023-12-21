# tutorial from https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
from typing import Any
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget 
import sys # to access command line argument

#create a subclass of MainWindow (inherit from QMainWindow) to customized window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")       #set window title
        button = QPushButton("Press Me!")   #create widget button
        self.setCentralWidget(button)       #put the button widget inside window. (center full screen by default)

        self.setMinimumSize(QSize(400,400))   #fixed size. user cannot adjust window

# create instance of the app (once)
# sys.argv is necessary if we need to pass some argument/parameter to command line
# if we know for sure we wont be using CLI, then passing empty list to QApplication will work too.
app = QApplication([])
# app = QApplication(sys.argv)

# create a widget window
# windows is basically a place to hold your UI. need at least one.
# app will stop when the last window is closed.

#window = QWidget()
#window = QPushButton("Push Me.")
#window = QMainWindow()

window = MainWindow() #using our define subclass with customised property instead of default QMainWindow
window.show() #show the window, something like print

# start the event loop
# meaning the app will wait for users action (i.e the event) such as keyboard stroke, mouse click etc
# app will react based on users action via event handler.
app.exec()