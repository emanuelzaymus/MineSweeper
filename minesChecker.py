class MinesChecker:
    __directions = [
        {"x": 0, "y":-1},
        {"x": 1, "y":-1},
        {"x": 1, "y": 0},
        {"x": 1, "y": 1},
        {"x": 0, "y": 1},
        {"x":-1, "y": 1},
        {"x":-1, "y": 0},
        {"x":-1, "y":-1}
    ]

    def __setGameUnclickable(self, mines):
        for i in range(0, mines["rows"]):
            for j in range(0, mines["columns"]):
                mines["data"][i][j]["clickable"] = False
        return mines

    def __setIslandUnclickable(self, mines, y, x):
        field = mines["data"][y][x]
        if field["clickable"] and not field["marked"]:
            field["clickable"] = False
            if field["type"] == "empty":
                for direct in self.__directions:
                    if (0 <= x + direct["x"] < mines["columns"]) and (0 <= y + direct["y"] < mines["rows"]):
                        self.__setIslandUnclickable(mines, y + direct["y"], x + direct["x"])
        return mines

    def __won(self, mines):
        data = mines["data"]
        for i in range(0, mines["rows"]):
            for j in range(0, mines["columns"]):
                if data[i][j]["clickable"] and not (data[i][j]["type"] == "mine"):
                    return False
        return True

    def __addMissingFlags(self, mines):
        data = mines["data"]
        for i in range(0, mines["rows"]):
            for j in range(0, mines["columns"]):
                if data[i][j]["type"] == "mine":
                    data[i][j]["type"] = "flag"

    def __setFoundFlag(self, mines):
        for row in mines["data"]:
            for field in row:
                if field["type"] == "mine" and field["marked"]:
                    field["type"] = "flag"
                elif field["marked"]:
                    field["type"] = "x"

    def checkMines(self, mines):
        clickedX = mines["clickedX"]
        clickedY = mines["clickedY"]
        field = mines["data"][clickedY][clickedX]

        if field["type"] == "mine":
            field["type"] = "explosion"
            mines["message"] = "lost"
            self.__setFoundFlag(mines)
            return self.__setGameUnclickable(mines)

        if field["type"] == "empty":
            return self.__setIslandUnclickable(mines, clickedY, clickedX)

        field["clickable"] = False
        if self.__won(mines):
            self.__addMissingFlags(mines)
            mines["message"] = "won"
            return self.__setGameUnclickable(mines)

        return mines
