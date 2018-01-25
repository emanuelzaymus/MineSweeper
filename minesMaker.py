from random import randint
from copy import deepcopy


def __createEmptyTable(width, height):
    ret = []
    line = []
    for i in range(0, width):
        line.append({"type":"empty", "clickable":True})
    for i in range(0, height):
        ret.append(deepcopy(line))
    return ret

def __setRandomMines(table, countOfMines):
    i = 0
    while (i < countOfMines):
        randY = randint(0, len(table) - 1)
        randX = randint(0, len(table[0]) - 1)
        if table[randY][randX]["type"] == "mine":
            i -= 1
        else:
            table[randY][randX]["type"] = "mine"
        i += 1
    return table

def __fillFields(table):
    for y in range(0, len(table)):
        for x in range(0, len(table[0])):
            if not table[y][x]["type"] == "mine":
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= y+i < len(table) and 0 <= x+j < len(table[0]):
                            if (table[y + i][x + j]["type"] == "mine"):
                                count += 1
                if count > 0:
                    table[y][x]["type"] = count
            
    return table

def generateMines(width, height, countOfMines):
    ret = __createEmptyTable(width, height)
    ret = __setRandomMines(ret, countOfMines)
    ret = __fillFields(ret)
    return ret
