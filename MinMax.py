import copy
import MancalaBoard
import Game
import play
import time


def MinMax(MancalaBoard, heuristic):
    open = []
    fathers = []

    # board, move, father, mm

    save = (copy.deepcopy(MancalaBoard), None, None, 'min')
    open.append(save)

    start = time.time()

    for element in open:
        if time.time() - start > 1:
            break
        if element.mm == 'min' and not element.again and len(MancalaBoard.possibleMoves(element.board, 2)) != 0:
            for move in MancalaBoard.possibleMoves(element.board, 2):
                inter, t = MancalaBoard.doMove(element.board, move, 2)
                fils = (inter, move, element, 'max')
                if t != element.mm:
                    fils.again = True
                element.fils.append(fils)
                open.append(fils)
        elif element.mm == 'max' and not element.again and len(MancalaBoard.possibleMoves(element.board, 1)) != 0:
            for move in MancalaBoard.possibleMoves(element.board, 1):
                inter, t = MancalaBoard.doMove(element.board, move, 1)
                fils = (inter, move, element, 'min')
                if t != element.mm:
                    fils.again = True
                element.fils.append(fils)
                open.append(fils)
        elif element.mm == 'min' and element.again and len(MancalaBoard.possibleMoves(element.board, 1)) != 0:
            for move in MancalaBoard.possibleMoves(element.board, 1):
                inter, t = MancalaBoard.doMove(element.board, move, 1)
                fils = (inter, move, element, 'min')
                if t != element.mm:
                    fils.again = True
                element.fils.append(fils)
                open.append(fils)
        elif element.mm == 'max' and element.again and len(MancalaBoard.possibleMoves(element.board, 2)) != 0:
            for move in MancalaBoard.possibleMoves(element.board, 2):
                inter, t = MancalaBoard.doMove(element.board, move, 2)
                fils = (inter, move, element, 'max')
                if t != element.mm:
                    fils.again = True
                element.fils.append(fils)
                open.append(fils)

    while len(open) != 0:
        for element in open:
            if element.father not in fathers and element.father is not None:
                fathers.append(element.father)

        for element in open:
            if element not in fathers:
                element.value = eval(element.board, heuristic)

        for element in open:
            print(element.mm, element.value, element.fils)
            print('***************************************')

        for element in fathers:
            for element2 in open:
                if element2.father == element:
                    if element.value is None:
                        element.value = element2.value
                    elif element.mm == 'min' and element.value < element2.value:
                        element.value = element2.value
                    elif element.mm == 'max' and element.value > element2.value:
                        element.value = element2.value
        for element in open:
            print(element.mm, element.value, element.fils)
            print('***************************************')
        open = fathers
        fathers = []
    max = save.fils[0].value
    m = save.fils[0].move
    for element in save.fils:
        if element.value > max:
            max = element.value
            m = element.move
    print(m)
    return m
