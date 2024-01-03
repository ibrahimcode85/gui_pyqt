#this is similar to app_2 but we use the signal
# to change interface instead of just printing the value in terminal.
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
        self.button = QPushButton("Push Me")
        self.button.clicked.connect(self.the_button_was_clicked)  #linked it to the defined slot(i.e. the signal receiver)

        self.setCentralWidget(self.button) #set initial state of the widget based on default value
        

    # define handler when button is clicked (i.e clicked signal is receive from QPushBUtton)
    def the_button_was_clicked(self, checked):
        self.button.setText("You already clicked me.") #change the button text.
        self.button.setEnabled(False)                  #disable button call.
        self.setWindowTitle("I clicked, so i change the title.") #change the window title.
    

# create instance of app to hold event loop
app = QApplication(sys.argv)

# create mainWindow and show it
window = MainWindow()
window.show()

# run the event loop
app.exec()