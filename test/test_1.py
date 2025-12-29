import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tiles Calculator")

        button = QPushButton("Press Me!")

        button.setFixedSize(QSize(90, 90))

        self.setMinimumSize(QSize(450, 450))
        self.setMaximumSize(QSize(900, 900))

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
