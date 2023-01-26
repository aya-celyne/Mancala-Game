import Game
import MancalaBoard
import os
import pygame
import random
import math
from pygame import mixer

mancalaBoard = MancalaBoard.MancalaBoard()
game = Game.Game(2)


def pink_heuristic():
    def getFinishPoint(startpit):
        finishPit = startpit
        for _ in range(mancalaBoard.board[startpit]):
            finishPit = mancalaBoard.nextSeed[finishPit]
            if finishPit == 'store1':
                finishPit = mancalaBoard.nextSeed[finishPit]
        return finishPit

    possible = mancalaBoard.possibleMoves(2)
    if possible == []:
        return 'NOT MOVE'

    # search for a move that ends in an empty computer pit
    bestStart = []
    for move in mancalaBoard.possibleMoves(2):
        if getFinishPoint(move) != 'store2' and getFinishPoint(move) in mancalaBoard.indexP2 and mancalaBoard.board[getFinishPoint(move)] == 0:
            bestStart.append(move)

    if len(bestStart) != 0:
        # returns the pit with the most seeds
        return bestStart[random.randint(0, len(bestStart)-1)]
    else:  # search for a move that ends in a computer pit
        goodStart = []
        for move in mancalaBoard.possibleMoves(2):
            if getFinishPoint(move) != 'store2' and getFinishPoint(move) not in mancalaBoard.indexP1:
                goodStart.append(move)

        if len(goodStart) != 0:
            return goodStart[random.randint(0, len(goodStart)-1)]
        else:  # search for a move that ends in an empty player pit so that he loses advantage
            mehStart = []
            for move in mancalaBoard.possibleMoves(2):
                if getFinishPoint(move) != 'store2' and getFinishPoint(move) not in mancalaBoard.indexP2 and getFinishPoint(move) == 0:
                    mehStart.append(move)

            if len(mehStart) != 0:
                return mehStart[random.randint(0, len(mehStart)-1)]
            else:  # just search for a move
                badStart = []
                for move in mancalaBoard.possibleMoves(2):
                    badStart.append(move)
                return badStart[random.randint(0, len(badStart)-1)]


def cyan_heuristic():
    def getFinishPoint(startpit):
        finishPit = startpit
        for _ in range(mancalaBoard.board[startpit]):
            finishPit = mancalaBoard.nextSeed[finishPit]
            if finishPit == 'store2':
                finishPit = mancalaBoard.nextSeed[finishPit]
        return finishPit

    possible = mancalaBoard.possibleMoves(1)
    if possible == []:
        return 'NOT MOVE'

    # search for a move that ends in an empty computer pit
    bestStart = []
    for move in mancalaBoard.possibleMoves(1):
        if getFinishPoint(move) != 'store1' and getFinishPoint(move) in mancalaBoard.indexP1 and mancalaBoard.board[getFinishPoint(move)] == 0:
            bestStart.append(move)

    if len(bestStart) != 0:
        return bestStart[random.randint(0, len(bestStart)-1)]
    else:  # search for a move that ends in a computer pit
        goodStart = []
        for move in mancalaBoard.possibleMoves(1):
            if getFinishPoint(move) != 'store1' and getFinishPoint(move) not in mancalaBoard.indexP2:
                goodStart.append(move)

        if len(goodStart) != 0:
            return goodStart[random.randint(0, len(goodStart)-1)]
        else:  # search for a move that ends in an empty player pit so that he loses advantage
            mehStart = []
            for move in mancalaBoard.possibleMoves(1):
                if getFinishPoint(move) != 'store1' and getFinishPoint(move) not in mancalaBoard.indexP1 and getFinishPoint(move) == 0:
                    mehStart.append(move)

            if len(mehStart) != 0:
                return mehStart[random.randint(0, len(mehStart)-1)]
            else:  # just search for a move
                badStart = []
                for move in mancalaBoard.possibleMoves(1):
                    badStart.append(move)
                return badStart[random.randint(0, len(badStart)-1)]

# this is the function that changed


def humanTurn():
    startPoint = cyan_heuristic()
    mancalaBoard.board, mancalaBoard.turn = (
        mancalaBoard.doMove(startPoint, 1))
    SFX.play(mixer.Sound(
        SFX_COLLECTION[random.randint(0, len(SFX_COLLECTION)-1)]))


def computerTurn():
    startPoint = pink_heuristic()
    mancalaBoard.board, mancalaBoard.turn = (
        mancalaBoard.doMove(startPoint, 2))
    SFX.play(mixer.Sound(
        SFX_COLLECTION[random.randint(0, len(SFX_COLLECTION)-1)]))


# assets
BOARD = pygame.image.load(os.path.join('images', 'MancalaBoard.PNG'))
WIN_BOARD = pygame.image.load(os.path.join('images', 'Player_Win_Screen.PNG'))
WIN_BOARD_HOVER = pygame.image.load(
    os.path.join('images', 'Player_Win_Screen_hover.PNG'))
LOSE_BOARD = pygame.image.load(
    os.path.join('images', 'Computer_Win_Screen.PNG'))
LOSE_BOARD_HOVER = pygame.image.load(
    os.path.join('images', 'Computer_Win_Screen_hover.PNG'))
YOUR_TURN = pygame.image.load(os.path.join('images', 'turn_player.PNG'))
COMPUTER_TURN = pygame.image.load(os.path.join('images', 'turn_computer.PNG'))
PLAYABLE_PIT_CYAN = pygame.image.load(
    os.path.join('images', 'Playable_cyan.PNG'))
PLAYABLE_PIT_Pink = pygame.image.load(
    os.path.join('images', 'Playable_pink.PNG'))
PIT_NOT_EMPTY_PINK = pygame.image.load(
    os.path.join('images', 'Store_Filled_pink.PNG'))
PIT_NOT_EMPTY_CYAN = pygame.image.load(
    os.path.join('images', 'Store_Filled_cyan.PNG'))
COIN_SPADES_BIG = pygame.image.load(os.path.join('images', 'neon_spades.PNG'))
COIN_SPADES = pygame.transform.scale(COIN_SPADES_BIG, (30, 30))
COIN_CLUBS_BIG = pygame.image.load(os.path.join('images', 'neon_clubs.PNG'))
COIN_CLUBS = pygame.transform.scale(COIN_CLUBS_BIG, (30, 30))
COIN_DIAMONDS_BIG = pygame.image.load(
    os.path.join('images', 'neon_diamonds.PNG'))
COIN_DIAMONDS = pygame.transform.scale(COIN_DIAMONDS_BIG, (30, 30))
COIN_HEARTS_BIG = pygame.image.load(os.path.join('images', 'neon_hearts.PNG'))
COIN_HEARTS = pygame.transform.scale(COIN_HEARTS_BIG, (30, 30))
music_state = [pygame.transform.scale(pygame.image.load(os.path.join('images', 'Music_Paused.png')), (
    40, 40)), pygame.transform.scale(pygame.image.load(os.path.join('images', 'Music_Playing.png')), (40, 40))]
music_next = pygame.transform.scale(pygame.image.load(
    os.path.join('images', 'Music_Next.png')), (40, 40))

coins_list = [COIN_SPADES, COIN_CLUBS, COIN_DIAMONDS, COIN_HEARTS]

pink_numbas = []
cyan_numbas = []
for i in range(49):
    pink_numbas.append(pygame.transform.scale(pygame.image.load(
        os.path.join('images/counters', f'neon_pink_{i}.png')), (24, 31)))
    cyan_numbas.append(pygame.transform.scale(pygame.image.load(
        os.path.join('images/counters', f'neon_cyan_{i}.png')), (24, 31)))

pinkNumbasPos = {'L': (780, 225),
                 'K': (660, 225),
                 'J': (540, 225),
                 'I': (420, 225),
                 'H': (300, 225),
                 'G': (180, 225),
                 'store2': (60, 70)}

cyanNumbsPos = {'A': (180, 362),
                'B': (300, 362),
                'C': (420, 362),
                'D': (540, 362),
                'E': (660, 362),
                'F': (780, 362),
                'store1': (915, 70)}

circlesRadius = 43
circleColors = ["PINK", "WHITE", "BLACK", "BROWN", "RED", "GREEN"]
circlesPos = {'A': [circleColors[0], (200, 316)],
              'B': [circleColors[1], (320, 316)],
              'C': [circleColors[2], (440, 316)],
              'D': [circleColors[3], (560, 316)],
              'E': [circleColors[4], (680, 316)],
              'F': [circleColors[5], (800, 316)],
              }
PlayableCyanPos = {'A': (135, 250),
                   'B': (255, 250),
                   'C': (372, 250),
                   'D': (493, 250),
                   'E': (610, 250),
                   'F': (730, 250)}

PlayablePinkPos = {'G': (135, 105),
                   'H': (255, 105),
                   'I': (372, 105),
                   'J': (493, 105),
                   'K': (610, 105),
                   'L': (730, 105)}


slotPos = {'A': list(zip([random.randint(156 - (circlesRadius - 60), 156 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'B': list(zip([random.randint(275 - (circlesRadius - 60), 275 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'C': list(zip([random.randint(394 - (circlesRadius - 60), 394 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'D': list(zip([random.randint(513 - (circlesRadius - 60), 513 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'E': list(zip([random.randint(632 - (circlesRadius - 60), 632 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'F': list(zip([random.randint(750 - (circlesRadius - 60), 750 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(272 + (10), 272 + (circlesRadius - 12)*2) for _ in range(44)])),
           'store1': list(zip([random.randint(890, 890 + circlesRadius) for _ in range(44)], [random.randint(130, 126 + (circlesRadius - 12)*6) for _ in range(44)])),
           'L': list(zip([random.randint(750 - (circlesRadius - 60), 750 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'K': list(zip([random.randint(632 - (circlesRadius - 60), 632 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'J': list(zip([random.randint(513 - (circlesRadius - 60), 513 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'I': list(zip([random.randint(394 - (circlesRadius - 60), 394 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'H': list(zip([random.randint(275 - (circlesRadius - 60), 275 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'G': list(zip([random.randint(156 - (circlesRadius - 60), 156 + (circlesRadius - 25)*2) for _ in range(44)], [random.randint(126 + (10), 126 + (circlesRadius - 12)*2) for _ in range(44)])),
           'store2': list(zip([random.randint(40, 100) for _ in range(44)], [random.randint(130, 126 + (circlesRadius - 12)*6) for _ in range(44)]))
           }


def circleClicked(COO):
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    sqx = (x - COO[0])**2
    sqy = (y - COO[1])**2

    if math.sqrt(sqx + sqy) < circlesRadius:
        return True
    else:
        return False


def draw_coins():
    for key in mancalaBoard.board:
        for i in range(1, mancalaBoard.board[key]+1):
            WIN.blit(coins_list[i % len(coins_list)], slotPos[key][i-1])

    for key in pinkNumbasPos:
        WIN.blit(pink_numbas[mancalaBoard.board[key]], pinkNumbasPos[key])
    for key in cyanNumbsPos:
        WIN.blit(cyan_numbas[mancalaBoard.board[key]], cyanNumbsPos[key])


paused = False


def pauseMusic(BGM):
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    global paused
    if x > 910 and x < 950 and y > 20 and y < 60:
        if pause == False:
            BGM.pause()
            paused = True
            return True
        else:
            BGM.unpause()
            paused = False
            return False


def changeMusic(BGM):
    global paused
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    if x > 865 and x < 905 and y > 20 and y < 60:
        BGM.stop()
        BGM.play(mixer.Sound(BGM_collections[random.randint(
            0, len(BGM_collections)-1)]), loops=-1)
        paused = False
        BGM.set_volume(0.8)


def draw_window(gameOver):
    if gameOver == False:
        WIN.blit(BOARD, (0, 0))
        draw_coins()
        # pits
        for key in PlayableCyanPos:
            if mancalaBoard.board[key] != 0:
                WIN.blit(PLAYABLE_PIT_CYAN, PlayableCyanPos[key])

        for key in PlayablePinkPos:
            if mancalaBoard.board[key] != 0:
                WIN.blit(PLAYABLE_PIT_Pink, PlayablePinkPos[key])

        if mancalaBoard.board['store1'] != 0:
            WIN.blit(PIT_NOT_EMPTY_CYAN, (840, 95))
        if mancalaBoard.board['store2'] != 0:
            WIN.blit(PIT_NOT_EMPTY_PINK, (-15, 95))

        # turn
        if mancalaBoard.turn == 1:
            WIN.blit(YOUR_TURN, (150, 40))
        elif mancalaBoard.turn == 2:
            WIN.blit(COMPUTER_TURN, (150, 40))
    elif mancalaBoard.board['store1'] > mancalaBoard.board['store2']:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x > 341 and x < 653 and y < 375 and y > 265:
            WIN.blit(WIN_BOARD_HOVER, (0, 0))
        else:
            WIN.blit(WIN_BOARD, (0, 0))
    else:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x > 341 and x < 653 and y < 375 and y > 265:
            WIN.blit(LOSE_BOARD_HOVER, (0, 0))
        else:
            WIN.blit(LOSE_BOARD, (0, 0))

    # music
    WIN.blit(music_next, (865, 20))
    if paused:
        WIN.blit(music_state[1], (910, 20))
    else:
        WIN.blit(music_state[0], (910, 20))
    pygame.display.update()


if __name__ == '__main__':

    WIDTH, HIEGHT = 1000, 400
    WIN = pygame.display.set_mode((WIDTH, HIEGHT))
    pygame.display.set_caption('Mancala Game computer vs computer')
    FPS = pygame.time.Clock()
    run = True

    # music
    mixer.init()
    BGM = pygame.mixer.Channel(0)
    BGM_collections = []
    for i in range(12):
        BGM_collections.append(mixer.Sound(
            os.path.join('music', f'music_{i}.mp3')))
    BGM.play(mixer.Sound(
        BGM_collections[random.randint(0, len(BGM_collections)-1)]))
    BGM.set_volume(0.8)
    pause = False

    # sound effects
    SFX = pygame.mixer.Channel(1)
    SFX_COLLECTION = []
    for i in range(1, 8):
        SFX_COLLECTION.append(mixer.Sound(
            os.path.join('sfx', f'sfx_0{i}.mp3')))

    while run:
        FPS.tick(60)
        for event in pygame.event.get():
            over, mancalaBoard.board = game.gameOver(mancalaBoard.board)
            if event.type == pygame.QUIT:
                run = False

            if not over and mancalaBoard.turn == 1:
                humanTurn()
            elif not over and mancalaBoard.turn == 2:
                computerTurn()
            elif over:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 341 and x < 653 and y < 375 and y > 265 and event.type == pygame.MOUSEBUTTONDOWN:
                    over = False
                    mancalaBoard.board = {'A': 4,
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
                    turn = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause = pauseMusic(BGM)
                changeMusic(BGM)

        draw_window(over)

    pygame.quit()
