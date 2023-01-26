import pygame

class MancalaBoard:

    def __init__(self):

        self.board = {'A': 4,
                      'B': 4,
                      'C': 4,
                      'D': 4,
                      'E': 4,
                      'F': 4,
                      'store1': 0,
                      'L': 4,
                      'K': 4,
                      'J': 4,
                      'I': 4,
                      'H': 4,
                      'G': 4,
                      'store2': 0}
        self.indexP1 = ('A', 'B', 'C', 'D', 'E', 'F')
        self.indexP2 = ('G', 'H', 'I', 'J', 'K', 'L')
        self.nextSeed = {'A': "B",
                         'B': "C",
                         'C': "D",
                         'D': "E",
                         'E': "F",
                         'F': "store1",
                         'store1': "L",
                         'L': "K",
                         'K': "J",
                         'J': "I",
                         'I': "H",
                         'H': "G",
                         'G': "store2",
                         'store2': "A"}
        self.oppositeSeed = {'A': 'G',
                             'B': 'H',
                             'C': 'I',
                             'D': 'J',
                             'E': 'K',
                             'F': 'L',
                             'L': 'F',
                             'K': 'E',
                             'J': 'D',
                             'I': 'C',
                             'H': 'B',
                             'G': 'A' }
        self.turn = 1

    def possibleMoves(self, turn):
        possiblemoves = []

        if turn == 1:
            for key in self.indexP1:
                if self.board[key] != 0:
                    possiblemoves.append(key)
        else :
            for key in self.indexP2:
                if self.board[key] != 0:
                    possiblemoves.append(key)

        return possiblemoves

    def doMove(self, startPoint, turn):
        if startPoint == 'NOT MOVE':
            turn = 1
            return self.board, turn
        ens = self.board[startPoint]
        self.board[startPoint] = 0
        match turn:
         case 1:
            turn = 2
            for _ in range (ens):
                if self.board != 'store2':
                    startPoint = self.nextSeed[startPoint]
                    self.board[startPoint] = self.board[startPoint] + 1
                    pygame.display.update()
            else:
                if startPoint in self.indexP1 and self.board[startPoint] == 1:
                    self.board['store1'] += self.board[self.oppositeSeed[startPoint]] + self.board[startPoint]
                    self.board[startPoint] = 0
                    self.board[self.oppositeSeed[startPoint]] = 0
                    turn = 1
                elif startPoint in self.indexP1:
                    turn = 1
         case 2:
            turn = 1
            for _ in range(ens):
                if self.board != 'store1':
                    startPoint = self.nextSeed[startPoint]
                    self.board[startPoint] = self.board[startPoint] + 1
                    pygame.display.update()
            else:
                if startPoint in self.indexP2 and self.board[startPoint] == 1:
                    self.board['store2'] += self.board[self.oppositeSeed[startPoint]] + self.board[startPoint]
                    self.board[startPoint] = 0
                    self.board[self.oppositeSeed[startPoint]] = 0
                    turn = 2
                elif startPoint in self.indexP2:
                    turn = 2
        
        return self.board, turn