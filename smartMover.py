import random
import chess

board= chess.Board()
class Player:
    def __init__(self, board, color, time):
        pass
    
    def move(self, board, time):
        return random.choice(list(board.legal_moves))
    def evalfunction(self,board):
        P=100
        N=320
        B=330
        R=500
        Q=900
        wp=len(board.pieces(chess.PAWN, chess.WHITE))
        bp=len(board.pieces(chess.PAWN, chess.BLACK))
        wn=len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn=len(board.pieces(chess.KNIGHT, chess.BLACK))
        wb=len(board.pieces(chess.BISHOP, chess.WHITE))
        bb=len(board.pieces(chess.BISHOP, chess.BLACK))
        wr=len(board.pieces(chess.ROOK, chess.WHITE))
        br=len(board.pieces(chess.ROOK, chess.BLACK))
        wq=len(board.pieces(chess.QUEEN, chess.WHITE))
        bq=len(board.pieces(chess.QUEEN, chess.BLACK))
        eval=P*(wp-bp)+N*(wn-bn)+B*(wb-bb)*R*(wr-br)+Q*(wq-bq)
        
        if (board.is_checkmate()):
            return -1e6
        else if (board.is_stalemate()):
            return 0
        else:
            if (board.turn):
                return eval
            return -eval
        
        