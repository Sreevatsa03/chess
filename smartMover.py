import random
import chess
import time

class Player:
    board = chess.Board()

    def __init__(self, board, color, time):
        pass
    
    def move(self, board, time):
        minValue = float("inf")
        minMove = None
        for move in board.legal_moves:
            copyBoard = board.copy()
            copyBoard.push(move)
            value = minimax(copyBoard, 2, float("-inf"), float("inf"), False)

            if value < minValue:
                minValue = value
                minMove = move


def evaluation(board):
        P = 100
        N = 320
        B = 330
        R = 500
        Q = 900
        wp = len(board.pieces(chess.PAWN, chess.WHITE))
        bp = len(board.pieces(chess.PAWN, chess.BLACK))
        wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
        bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
        wb = len(board.pieces(chess.BISHOP, chess.WHITE))
        bb = len(board.pieces(chess.BISHOP, chess.BLACK))
        wr = len(board.pieces(chess.ROOK, chess.WHITE))
        br = len(board.pieces(chess.ROOK, chess.BLACK))
        wq = len(board.pieces(chess.QUEEN, chess.WHITE))
        bq = len(board.pieces(chess.QUEEN, chess.BLACK))
        eval = P * (wp - bp) + N * (wn - bn) + B * (wb - bb) * R * (wr - br) + Q * (wq - bq)
        
        if board.is_checkmate():
            return -1e6
        elif board.is_stalemate():
            return 0
        else:
            if board.turn:
                return eval
            return -eval
    
def minimax(board, depth, alpha, beta, isMax):
    if board.is_checkmate():
        return -40 if isMax else 40
    elif board.is_game_over():
        return 0

    if depth == 0:
        return evaluation(board)

    if isMax:
        bestValue = float("-inf")
        for move in board.legal_moves:
            copyBoard = board.copy()
            copyBoard.push(move)
            value = minimax(copyBoard, depth, alpha, beta, False)
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)
            if alpha >= beta:
                break
        return bestValue
    else:
        bestValue = float("inf")
        for move in board.legal_moves:
            copyBoard = board.copy()
            copyBoard.push(move)
            value = minimax(copyBoard, depth - 1, alpha, beta, True)
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)
            if alpha >= beta:
                break
        return bestValue

    return 0