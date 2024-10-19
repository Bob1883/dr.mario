def moveBlock(gameMap:list, direction:int) -> list:
    height = len(gameMap)
    width = len(gameMap[0])
    
    # moving right
    if direction == 1:  
        col_range = range(width - 1, -1, -1)

    # moving left
    else:  
        col_range = range(width)

    for row in range(height - 1, -1, -1):
        for col in col_range:
            if gameMap[row][col].startswith("a "):
                newCol = col + direction
                if 0 <= newCol < width and gameMap[row][newCol] == "*":
                    gameMap[row][newCol] = gameMap[row][col]
                    gameMap[row][col] = "*"

    return gameMap

def moveDown(gameMap: list) -> list:
    height = len(gameMap)
    width = len(gameMap[0])

    can_move = True
    for row in range(height - 1, -1, -1):
        for col in range(width):
            if gameMap[row][col].startswith("a "):
                if row == height - 1 or not gameMap[row + 1][col] in ["*", gameMap[row][col]]:
                    can_move = False
                    break
        if not can_move:
            break

    if can_move:
        for row in range(height - 2, -1, -1):
            for col in range(width):
                if gameMap[row][col].startswith("a "):
                    gameMap[row + 1][col] = gameMap[row][col]
                    gameMap[row][col] = "*"
    else:
        for row in range(height):
            for col in range(width):
                if gameMap[row][col].startswith("a "):
                    gameMap[row][col] = gameMap[row][col][2:]

    return gameMap

# TODO: fix rotation
def rotateBlock(gameMap:list) -> list:
    return gameMap