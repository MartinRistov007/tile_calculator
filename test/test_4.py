from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    "My Tiles Calculator Application",
    "My TC App",
    "Ceramics Tiles and Stone Tiles Calculator",
    "Tiles Calculator 2 confirmed?!",
    "Tiles Calculator by Aleksandar Janjus",
    "Made with love and passion",
    "Incredible possibilities within the app",
    "Buy one get 10 free!!!!!",
    ":D :D :D :D :D :D",
    "A◘py╘$EÅ21¥16T╘13♪A♦45☺3186451╝356♦5ú3☺41A1w35♪1☻1░5╤132",
    "Testing",
    "Okay we stop now",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("Tiles Calculator")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Okay we stop now":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()