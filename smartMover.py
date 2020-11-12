import random
import chess
import time

class Player:
    board = chess.Board()

    def __init__(self, board, color, time):
        pass
    
    def move(self, board, time):
        bestMove = self.minimax(board, self.player, self.depth)

        return bestMove[1]

    def evalfunction(board):
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
        elif (board.is_stalemate()):
            return 0
        else:
            if (board.turn):
                return eval
            return -eval
    
    def minimax(self, board, player, depth, alpha, beta):
        if (depth == 0 or game_over(board)):
            return [game_score(board, self.player, END_SCORES, BOARD_SCORES), None]
        
        moves = sorted_moves(board)

        if (board.turn == player):
            maxScore, bestMove = -inf, None

            for move, piece in moves:
                copyBoard = board.copy()
                copyBoard.push(move)

                score = self.minimax(copyBoard, not player, depth - 1, alpha, beta)

                alpha = max(alpha, score[0])
                if (beta <= alpha):
                    break

                if (score[0] >= maxScore):
                    maxScore = score[0]
                    bestMove = move

            return [maxScore, bestMove]
        else: 
            minScore, bestMove = inf, None

            for move, piece in moves:
                copyBoard = board.copy()
                copyBoard.push(move)

                score = self.minimax(copyBoard, player, depth - 1, alpha, beta)

                beta = min(beta, score[0])
                if (beta <= alpha):
                    break

                if (score[0] <= minScore):
                    minScore = score[0]
                    bestMove = move

            return [minScore, bestMove]