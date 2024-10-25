import random as r 

def plotRandomVirus(gameMap:list, level:int) -> list: 
    amount = level * r.randint(1, 2)

    if amount > ((len(gameMap)-2)*len(gameMap[0]))/1.1: 
        amount = int((len(gameMap)*len(gameMap[0]))/1.1)

    colors = {1: "b", 2: "g", 3: "r", 4: "y"}

    for n in range(amount): 
        while True: 
            x = r.randint(4, len(gameMap)-1)
            y = r.randint(0, len(gameMap[0])-1)

            if gameMap[x][y] == "*": 
                gameMap[x][y] = "v " + colors[r.randint(1, 4)]
                break

    return gameMap

# if __name__ == "__main__": 
#     from createMap import createMap
#     from drawMap import drawMap

#     gameMap = createMap(5, 5)
#     gameMap = plotRandomVirus(gameMap, 3)
#     drawMap(gameMap, 1, 1, 1)

