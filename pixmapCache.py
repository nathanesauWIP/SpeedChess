from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

COLOR_NONE = -1
COLOR_WHITE = 0
COLOR_BLACK = 1

PIECE_NONE = -1
PIECE_PAWN = 0
PIECE_KNIGHT = 1
PIECE_BISHOP = 2
PIECE_ROOK = 3
PIECE_QUEEN = 4
PIECE_KING = 5


class PixmapCache:
    def __init__(self):
        self.pixmaps = {}
        self.files = {(COLOR_WHITE, PIECE_PAWN): ":WhitePawn.png",
                      (COLOR_WHITE, PIECE_KNIGHT): ":WhiteKnight.png",
                      (COLOR_WHITE, PIECE_BISHOP): ":WhiteBishop.png",
                      (COLOR_WHITE, PIECE_ROOK): ":WhiteRook.png",
                      (COLOR_WHITE, PIECE_QUEEN): ":WhiteQueen.png",
                      (COLOR_WHITE, PIECE_KING): ":WhiteKing.png",
                      (COLOR_BLACK, PIECE_PAWN): ":BlackPawn.png",
                      (COLOR_BLACK, PIECE_KNIGHT): ":BlackKnight.png",
                      (COLOR_BLACK, PIECE_BISHOP): ":BlackBishop.png",
                      (COLOR_BLACK, PIECE_ROOK): ":BlackRook.png",
                      (COLOR_BLACK, PIECE_QUEEN): ":BlackQueen.png",
                      (COLOR_BLACK, PIECE_KING): ":BlackKing.png"}

    def getPixmap(self, color, piece):
        if (color, piece) in self.files:
            if (color, piece) in self.pixmaps:
                return self.pixmaps[(color, piece)]
            else:
                pixmap = QPixmap(self.files[(color, piece)])
                self.pixmaps[(color, piece)] = pixmap
                return pixmap
        else:
            return QPixmap()
