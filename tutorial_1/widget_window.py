from PyQt6.QtWidgets import QApplication, QWidget
import sys

# short example of executing GUI windows as widget

app = QApplication(sys.argv)
window = QWidget()

window.show()

sys.exit(app.exec())
