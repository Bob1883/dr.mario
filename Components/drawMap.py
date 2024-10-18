def drawMap(gameMap:list, game_time:int, level:int, score:int) -> list:
    print("\033[H\033[J", end="")  

    BLUE = "\033[34m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    COLORS = {"b": BLUE, "g": GREEN, "r": RED, "y": YELLOW}
    num_columns = len(gameMap)
    num_rows = len(gameMap[0])
    map_width = num_columns * 2 + 3 

    output_lines = []
    output_lines.append("-" * map_width)

    for row in range(num_rows):
        line = "| "
        for column in range(num_columns):
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

                gameMap[row][column] = f"{parts[1]} {parts[0]}"

            else:
                line += "? "

        line += "|"
        output_lines.append(line)

    output_lines.append("-" * map_width)

    total_lines = len(output_lines)
    info_output_lines = [""] * total_lines

    info_output_lines[1] = f" Level: {level}"
    info_output_lines[2] = f" Score: {score}"
    info_output_lines[3] = f" Time: {game_time}s"

    for i in range(total_lines):
        map_line = output_lines[i]
        info_line = info_output_lines[i]
        print(map_line.ljust(map_width) + "   " + info_line)

    return gameMap

if __name__ == "__main__":
    import time as t

    HEIGHT = 10
    WIDTH = 10
    gameMap = [
        ["*", "b", "b", "*", "*"],
        ["*", "v b", "v b", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "a b", "a r", "*", "*"],
        ["*", "*", "*", "*", "*"],
    ]

    level = 1
    score = 0
    startTime = t.time()

    for _ in range(10):
        gameTime = int(t.time() - startTime)
        drawMap(gameMap, gameTime, level, score)
        t.sleep(1)
