from PyQt6.QtWidgets import QApplication, QWidget
import sys

# short example of executing GUI windows (using widget as example.
# other item includes QMainWindow and QDialog)
app = QApplication(sys.argv)
window = QWidget()

window.show()

sys.exit(app.exec())
