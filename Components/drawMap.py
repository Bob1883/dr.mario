def drawMap(gameMap:list, gameTime:int, level:int, score:int, mainLoop:str=False) -> list:
    print("\033[H\033[J", end="")  

    BLUE = "\033[34m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    COLORS = {"b": BLUE, "g": GREEN, "r": RED, "y": YELLOW}
    numColumns = len(gameMap)
    numRows = len(gameMap[0])
    mapWidth = numColumns * 2 + 3 

    outputLines = []
    outputLines.append("-" * mapWidth)

    for row in range(numRows):
        line = "| "
        for column in range(numColumns):
            tile = gameMap[row][column].replace("a ", "")

            if tile == "*":
                line += "  "

            elif tile in COLORS:
                line += f"{COLORS[tile]}■{RESET} "

            elif "v" in tile:
                parts = tile.split(" ")
                if parts[0] == "v":
                    color = COLORS.get(parts[1], RESET)
                    line += f"{color}■{RESET} "

                else:
                    color = COLORS.get(parts[0], RESET)
                    line += f"{color}#{RESET} "

                if mainLoop:
                    gameMap[row][column] = f"{parts[1]} {parts[0]}"

            else:
                line += "? "

        line += "|"
        outputLines.append(line)

    outputLines.append("-" * mapWidth)

    totalLines = len(outputLines)
    infoOutputLines = [""] * totalLines

    infoOutputLines[1] = f" Level: {level}"
    infoOutputLines[2] = f" Score: {score}"
    infoOutputLines[3] = f" Time: {gameTime}s"

    for i in range(totalLines):
        mapLine = outputLines[i]
        infoLine = infoOutputLines[i]
        print(mapLine.ljust(mapWidth) + "   " + infoLine)

    return gameMap

# if __name__ == "__main__":
#     import time as t

#     HEIGHT = 10
#     WIDTH = 10
#     gameMap = [
#         ["*", "b", "b", "*", "*"],
#         ["*", "v b", "v b", "*", "*"],
#         ["*", "*", "*", "*", "*"],
#         ["*", "a b", "a r", "*", "*"],
#         ["*", "*", "*", "*", "*"],
#     ]

#     level = 1
#     score = 0
#     startTime = t.time()

#     for i in range(10):
#         gameTime = int(t.time() - startTime)
#         drawMap(gameMap, gameTime, level, score)
#         t.sleep(1)
