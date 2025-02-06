import random

class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, board):
        raise NotImplementedError("This method should be overridden by subclasses")

class AIPlayer(Player):
    def make_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = self.minimax(board, 0, False)
                    board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, 'O'):
            return 1
        elif self.check_winner(board, 'X'):
            return -1
        elif not any('' in row for row in board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_conditions:
            if board[a//3][a%3] == board[b//3][b%3] == board[c//3][c%3] == player:
                return True
        return False