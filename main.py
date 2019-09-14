# icons
# https://marcelk.net/chess/pieces/alpha.zip

import sys
from PyQt5.QtWidgets import * # pip install PyQt5
from PyQt5.QtGui import *
from mainWindow import *
import qrc_resources # pyrcc5 resources.qrc -o qrc_resources.py

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.setWindowTitle("Speed Chess")
    mainWindow.resize(600, 700)
    mainWindow.setWindowIcon(QIcon(":BlackKing.png"))
    mainWindow.show()

    app.exec()