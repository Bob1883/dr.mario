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

    # Find active blocks
    active_blocks = []
    for row in range(height):
        for col in range(width):
            if gameMap[row][col].startswith("a "):
                active_blocks.append((row, col, gameMap[row][col]))

    if len(active_blocks) != 2:
        # Cannot rotate without exactly two active blocks
        return gameMap

    # Unpack active blocks
    (row1, col1, val1), (row2, col2, val2) = active_blocks

    # Calculate the difference in positions
    dx = col2 - col1
    dy = row2 - row1

    # Determine current orientation
    if dx == 1 and dy == 0:
        state = 0  # Horizontal, block2 is right of block1
    elif dx == 0 and dy == 1:
        state = 1  # Vertical, block2 is below block1
    elif dx == -1 and dy == 0:
        state = 2  # Horizontal, block2 is left of block1
    elif dx == 0 and dy == -1:
        state = 3  # Vertical, block2 is above block1
    else:
        # Blocks are not adjacent; cannot rotate
        return gameMap

    # Calculate next rotation state
    next_state = (state + 1) % 4

    # Compute new position for block2 based on rotation
    if next_state == 0:
        new_row2 = row1
        new_col2 = col1 + 1
    elif next_state == 1:
        new_row2 = row1 + 1
        new_col2 = col1
    elif next_state == 2:
        new_row2 = row1
        new_col2 = col1 - 1
    elif next_state == 3:
        new_row2 = row1 - 1
        new_col2 = col1
    else:
        # Invalid state; should not happen
        return gameMap

    # Check if new position is within bounds and empty
    if 0 <= new_row2 < height and 0 <= new_col2 < width and gameMap[new_row2][new_col2] == "*":
        # Update game map with new positions
        gameMap[row2][col2] = "*"
        gameMap[new_row2][new_col2] = val2
    else:
        # Rotation blocked; do nothing
        pass

    return gameMap
