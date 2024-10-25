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
def rotateBlock(gameMap: list) -> list:
    height = len(gameMap)
    width = len(gameMap[0])

    active_blocks = []
    for row in range(height):
        for col in range(width):
            if gameMap[row][col].startswith("a "):
                active_blocks.append((row, col, gameMap[row][col]))

    if len(active_blocks) != 2:
        return gameMap

    (row1, col1, block1), (row2, col2, block2) = active_blocks

    if row1 == row2:
        base_row = row1
        base_col = min(col1, col2)  

        new_row = base_row + 1
        new_col = base_col

        if new_row < height and gameMap[new_row][new_col] == "*":
            gameMap[row1][col1] = "*"
            gameMap[row1][col2] = "*"

            left_block = block1 if col1 == base_col else block2
            right_block = block2 if col1 == base_col else block1

            gameMap[base_row][base_col] = left_block
            gameMap[new_row][new_col] = right_block
    else:
        base_row = max(row1, row2)  
        base_col = col1 if row1 == base_row else col2

        new_row = base_row
        new_col = base_col + 1

        if new_col < width and gameMap[new_row][new_col] == "*":
            gameMap[row1][col1] = "*"
            gameMap[row2][col2] = "*"

            bottom_block = block1 if row1 == base_row else block2
            top_block = block2 if row1 == base_row else block1

            gameMap[base_row][base_col] = bottom_block
            gameMap[new_row][new_col] = top_block
        else:
            new_col = base_col - 1
            if new_col >= 0 and gameMap[new_row][new_col] == "*":
                gameMap[row1][col1] = "*"
                gameMap[row2][col2] = "*"

                gameMap[base_row][base_col] = bottom_block
                gameMap[new_row][new_col] = top_block

    return gameMap