from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player
        self.first_move = True

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.first_move = False


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        if self.first_move:
            available_moves = [1,2]        
        else: 
            available_moves = [1]
        available_squares = []
        for move in available_moves: 
            if self.player == Player.BLACK:
                square_in_front = Square.at(current_square.row - move, current_square.col)
                if not board.get_piece(square_in_front):
                    available_squares.append(square_in_front)
                else:
                    break
            else:
                square_in_front = Square.at(current_square.row + move, current_square.col)
                if not board.get_piece(square_in_front):
                    available_squares.append(square_in_front)
                else:
                    break
        return available_squares

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board) -> List[Square]:
        current_square = board.find_piece(self)
        
        current_col = current_square.col
        current_row = current_square.row

        available_cols = range(current_col-1, current_col+2)
        available_rows = range(current_row-1, current_row+2)

        available_squares = []

        for r in available_rows:
            if r < 0 or r > 7:
                continue
            for c in available_cols:
                if c < 0 or c > 7:
                    continue
                
                if r == current_row and c == current_col:
                    continue
                if not board.get_piece(Square.at(r, c)):
                    available_squares.append(Square.at(r, c))
                else:
                    pass
        return available_squares