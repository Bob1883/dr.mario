def isLevelCleared(gameMap:list) -> bool: 
    for slice in gameMap: 
        for tile in slice: 
            if "v" in tile: 
                return False 
            
    return True


if __name__ == "__main__": 
    gameMap = [
        ["*", "b", "b", "*", "*"],
        ["*", "b", "b", "*", "*"],
        ["*", "*", "*", "*", "*"],
        ["*", "b", "*", "*", "*"],
        ["*", "*", "*", "*", "*"],
    ]

    print(isLevelCleared(gameMap))