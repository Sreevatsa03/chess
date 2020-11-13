import random
import chess
import time

class Player:

    board = chess.Board()
    def __init__(self, board, color, time):
        pass
    
    def move(self, board, time):
        maxScore, bestMove = float("-inf"), None
        for move in board.legal_moves:
            copyBoard = board.copy()
            copyBoard.push(move)
            score = self.minimax(board, True, 1, float("-inf"), float("inf"))
            if score >= maxScore:
                maxScore = score
                bestMove = move
        return bestMove

    def evaluation(self, board):
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

    def minimax(self, board, isMax, depth, alpha, beta):
        if board.is_checkmate():
            return -40 if isMax else 40

        if depth == 0:
            return self.evaluation(board)

        if isMax:
            maxScore, bestMove = float("-inf"), None
            for move in board.legal_moves:
                copyBoard = board.copy()
                copyBoard.push(move)
                score = self.minimax(copyBoard, not isMax, depth - 1, alpha, beta)
                maxScore = max(score, maxScore)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return maxScore
        else: 
            minScore, bestMove = float("inf"), None
            for move in board.legal_moves:
                copyBoard = board.copy()
                copyBoard.push(move)
                score = self.minimax(copyBoard, isMax, depth - 1, alpha, beta)
                minScore = min(score, minScore)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return minScore