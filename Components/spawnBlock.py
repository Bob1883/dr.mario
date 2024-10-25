import random as r 

def spawnBlock(gameMap:list) -> list:
    maxLength = 2
    length = r.randint(1, int(maxLength/2)) * 2
    colors = {1: "b", 2: "g", 3: "r", 4: "y"}
    
    mapWidth = len(gameMap[0])
    startIndex = (mapWidth - length) // 2

    for i in range(0, length, 2):
        gameMap[0][startIndex + i] = "a " + colors[r.randint(1, 4)]
        gameMap[0][startIndex + i + 1] = "a " + colors[r.randint(1, 4)]

    return gameMap

# if __name__ == "__main__": 
#     from createMap import createMap
#     from drawMap import drawMap

#     gameMap = createMap(10, 10)

#     drawMap(spawnBlock(gameMap), 1, 1, 1)