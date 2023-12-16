from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()


window.statusBar().showMessage("Welcome to PyQT6 Course.")

#important!! for mac. a menu must have at least one action, otherwise it will not show. Below is effects on Mac .
#in this example, we sont see the 'File' menu eventhough the menu is added.
#source from stackoverflow :https://stackoverflow.com/questions/28559730/menu-entry-not-shown-on-mac-os

#adding menubar
#create menu bar and add to window
menu_bar = window.menuBar()

#create a menu
file_menu = menu_bar.addMenu("File")

#make menu bar visible
window.setMenuBar(menu_bar)

window.show()
sys.exit(app.exec())
