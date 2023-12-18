from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

#create a class an inherit if from QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700,400) #set the position where the window will pop-up; and the dimension of the window
        self.setWindowTitle("Python GUI window") #set the title of the window (appear at top of the window)
        self.setWindowIcon(QIcon("images/robot.jpg")) #suppose to set icon in the window header next to title..but not sure if this works for mac.
        # self.setFixedWidth(700) #width is fix, so user cannot resize
        # self.setFixedHeight(400) #same as FixedWidth

        self.setStyleSheet('background-color:black') #param like css?
        self.setWindowOpacity(0.5) #number from 0-1

app = QApplication(sys.argv)
window = Window()

window.show()

sys.exit(app.exec())