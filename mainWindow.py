from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pixmapCache import *

pixmapCache = PixmapCache()

class Square(QLabel):
    clicked = pyqtSignal(int, int)

    def __init__(self, row, col, color, piece, parent=None):
        super().__init__(parent)

        self.row = row
        self.col = col
        self.color = color
        self.piece = piece

        if (row + col) % 2:
            self.setStyleSheet("background-color: white")
        else:
            self.setStyleSheet("background-color: brown")

        pixmap = pixmapCache.getPixmap(color, piece)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        self.clicked.emit(self.row, self.col)


class Board(QWidget):
    def getInitialColorPiece(self, row, col):
        color = COLOR_BLACK if (row is 0 or row is 1) \
            else COLOR_WHITE if (row is 6 or row is 7) \
            else COLOR_NONE

        if color is not COLOR_NONE:
            piece = PIECE_PAWN if (row is 1 or row is 6) \
                else PIECE_ROOK if (col is 0 or col is 7) \
                else PIECE_KNIGHT if (col is 1 or col is 6) \
                else PIECE_BISHOP if (col is 2 or col is 5) \
                else PIECE_QUEEN if (col is col is 3) \
                else PIECE_KING
        else:
            piece = PIECE_NONE

        return (color, piece)

    def __init__(self, parent=None):
        super().__init__(parent)
        mainLayout = QGridLayout()  # 8 x 8
        for row in range(0, 8, 1):
            for col in range(0, 8, 1):
                colorPiece = self.getInitialColorPiece(row, col)
                square = Square(row, col, colorPiece[0], colorPiece[1])
                square.clicked.connect(self.onClicked)
                mainLayout.addWidget(square, row, col)

        self.setLayout(mainLayout)

    def onClicked(self, row, col):
        print(row, ", ", col, " clicked!")


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        board = Board()  # 8 x 8
        self.setCentralWidget(board)
