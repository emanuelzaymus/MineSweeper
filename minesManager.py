from minesMaker import generateMines


class MinesManager:

    __levels = [
        {'width': 9, 'height': 9, 'countOfMines': 10},
        {'width': 15, 'height': 10, 'countOfMines': 30},
        {'width': 20, 'height': 15, 'countOfMines': 50}
    ]

    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__countOfMines = 0
        self.__level = 0

    def __setLevel(self):
        level = self.__level % len(self.__levels)
        self.__width = self.__levels[level]['width']
        self.__height = self.__levels[level]['height']
        self.__countOfMines = self.__levels[level]['countOfMines']
        self.__level += 1

    def getMines(self):
        self.__setLevel()
        gameData = { 
            'columns': self.__width,
            'rows': self.__height,
            'countOfMines': self.__countOfMines,
            'message': '',
            'clickedX': -1,
            'clickedY': -1,
            'data': generateMines(self.__width, self.__height, self.__countOfMines)
        }
        return gameData
