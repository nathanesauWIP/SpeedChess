from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pixmapCache import *

pixmapCache = PixmapCache()


class Square(QLabel):
    clicked = pyqtSignal(QLabel)

    def refreshStyleSheet(self):
        if (self.row + self.col) % 2:
            self.setStyleSheet("background-color: white")
        else:
            self.setStyleSheet("background-color: brown")

    def refreshPixmap(self):
        self.setPixmap(pixmapCache.getPixmap(self.color, self.piece))

    def __init__(self, row, col, color, piece, parent=None):
        super().__init__(parent)

        self.row = row
        self.col = col
        self.color = color
        self.piece = piece

        self.refreshStyleSheet()
        self.refreshPixmap()

    def mousePressEvent(self, event):
        self.clicked.emit(self)


class Board(QWidget):
    def getInitialColorPiece(row, col):
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
                colorPiece = Board.getInitialColorPiece(row, col)
                square = Square(row, col, colorPiece[0], colorPiece[1])
                square.clicked.connect(self.onClicked)
                mainLayout.addWidget(square, row, col)
        self.setLayout(mainLayout)

        self.highlightedSquare = None

    def onClicked(self, square):
        if self.highlightedSquare:
            self.highlightedSquare.refreshStyleSheet()

        if square.color is COLOR_WHITE or square.color is COLOR_BLACK:
            square.setStyleSheet("background-color: lightblue")
            self.highlightedSquare = square
        else:  # try to move self.highlightedSquare to square
            if self.highlightedSquare:
                square.color = self.highlightedSquare.color
                square.piece = self.highlightedSquare.piece
                square.refreshPixmap()

                if self.highlightedSquare.row is not square.row or \
                        self.highlightedSquare.col is not square.col:
                    self.highlightedSquare.color = COLOR_NONE
                    self.highlightedSquare.piece = PIECE_NONE
                    self.highlightedSquare.refreshPixmap()
                
                self.highlightedSquare = None

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        board = Board()  # 8 x 8
        self.setCentralWidget(board)
