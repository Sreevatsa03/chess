import random
import chess

board= chess.Board()
class Player:
    def __init__(self, board, color, time):
        pass
    
    def move(self, board, time):
        return random.choice(list(board.legal_moves))
    def evalfunction(self,board):
        return board.legal_moves.count()
        
        