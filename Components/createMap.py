def createMap(height:int, width:int) -> list: 
    gameMap = []
    for row in range(height): 
        gameMap.append([])
        for column in range(width): 
            gameMap[row].append("*")

    return(gameMap)

if __name__ == "__main__": 
    print(createMap(5, 5))
