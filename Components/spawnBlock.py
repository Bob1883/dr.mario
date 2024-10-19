import random as r 

def spawnBlock(gameMap:list, maxLength:int=4) -> list:
    length = r.randint(1, int(maxLength/2)) * 2
    colors = {1: "b", 2: "g", 3: "r", 4: "y"}
    
    mapWidth = len(gameMap[0])
    startIndex = (mapWidth - length) // 2

    color1 = colors[r.randint(1, 4)]
    color2 = color1
    while color2 == color1:
        color2 = colors[r.randint(1, 4)]

    for i in range(0, length, 2):
        if i == 0: 
            gameMap[0][startIndex + i] = "a " + color1
            gameMap[0][startIndex + i + 1] = "a " + color1
        else: 
            gameMap[0][startIndex + i] = "a " + color2
            gameMap[0][startIndex + i + 1] = "a " + color2

    return gameMap

# if __name__ == "__main__": 
#     from createMap import createMap
#     from drawMap import drawMap

#     gameMap = createMap(10, 10)

#     drawMap(spawnBlock(gameMap), 1, 1, 1)