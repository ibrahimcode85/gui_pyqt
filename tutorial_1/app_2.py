# tutorial from https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
# on signals on slot (define app action upon user event)

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# create subclass to customize QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # add a default state
        self.button_is_checked = True

        # add window title
        self.setWindowTitle("My App 2")

        # add a push button widget into the main window
        button = QPushButton("Push Me")
        button.setCheckable(True)                            #this is to set the state can be toggled between True and False. Otherwise it is always false.
        button.clicked.connect(self.the_button_was_toggled)  #linked it to the defined action
        button.setChecked(self.button_is_checked)
        self.setCentralWidget(button) #set initial state of the widget based on default value
        

    # define handler when button is clicked (i.e clicked signal is receive from QPushBUtton)
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked # update state when button is clicked
        print(self.button_is_checked)
    

# create instance of app to hold event loop
app = QApplication(sys.argv)

# create mainWindow and show it
window = MainWindow()
window.show()

# run the event loop
app.exec()