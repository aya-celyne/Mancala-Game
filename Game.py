from sre_parse import State
import MancalaBoard


class Game:
    def __init__(self, playerSide):
        self.state = MancalaBoard.MancalaBoard()
        self.playerSide = playerSide

    def gameOver(self, board):
        over = True
        self.state.board = board.copy()
        for i in self.state.indexP1:
            if self.state.board[i] != 0:
                over = False
                break
        else:
            for j in self.state.indexP2:
                self.state.board['store2'] += self.state.board[j]
                self.state.board[j] = 0

        for i in self.state.indexP2:
            if self.state.board[i] != 0:
                over = False
                break
        else:
            for j in self.state.indexP1:
                self.state.board['store1'] += self.state.board[j]
                self.state.board[j] = 0

        return over, self.state.board

    def findWinner(self):

        if self.state.board['store1'] > self.state.board['store2']:
            return 1  # you win
        elif self.state.board['store1'] < self.state.board['store2']:
            return 2  # computer wins
        else:
            return 0  # draw very rare
