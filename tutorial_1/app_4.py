#another example of using the signal to modify window title

import sys
from random import choice
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

# set list of titles to randomly choose from
window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

#create subclass for our app
class MainWindow(QMainWindow):
    def __init__(self):
    
        super().__init__() #inherit initial value from parent

        self.n_times_clicked = 0
        self.setWindowTitle("MyApp 4")
        self.button = QPushButton("Press Me!")

        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        self.setWindowTitle(new_window_title)
        print(f"Setting title: {new_window_title}.")

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}.")

        if window_title ==  "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()