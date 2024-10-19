def dropBlock(gameMap:list) -> list:
    numRows = len(gameMap)
    numCols = len(gameMap[0])

    activeBlocks = []

    for row in range(numRows):
        for col in range(numCols):
            tile = gameMap[row][col]
            if tile.startswith('a '):
                activeBlocks.append((row, col))

    canMove = True
    for row, col in activeBlocks:
        nextRow = row + 1
        if nextRow >= numRows or gameMap[nextRow][col] != '*':
            canMove = False
            break

    if canMove:
        for row, col in sorted(activeBlocks, reverse=True):
            tile = gameMap[row][col]
            gameMap[row][col] = '*'
            gameMap[row + 1][col] = tile
    else:
        for row, col in activeBlocks:
            tile = gameMap[row][col]
            gameMap[row][col] = tile[2:] 

    return gameMap
