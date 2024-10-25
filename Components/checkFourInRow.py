def removeDups(array:list) -> list: 
    newArray = []
    for subList in array:
        if subList not in newArray:
            newArray.append(subList)
    return newArray  

def inverseMap(gameMap:list) -> list: 
    newMap = []

    for i in range(len(gameMap)):
        mapSlice = []
        for n in range(len(gameMap[0])): 
            mapSlice.append(gameMap[n][i])

        newMap.append(mapSlice)

    return newMap

#TODO: change to better name
def checkToRemove(mapSlice:list) -> list: 
    colors = ["b", "g", "r", "y"]
    toRemove = []

    for height in range(len(mapSlice)): 
        for color in colors: 
            count = 0 
            for width in range(len(mapSlice[0])): 
                if color in mapSlice[height][width] and "a" not in mapSlice[height][width]: 
                    count += 1
                else: 
                    count = 0 

                if count >= 4: 
                    for i in range(4): 
                        toRemove.append([height, width-i])
    
    return toRemove

def checkFourInRow(gameMap:list, score:int) -> tuple: 
    toRemove = []

    inverse = inverseMap(gameMap)
    vertical = checkToRemove(inverse) 
    horizontal = checkToRemove(gameMap)

    for n in range(len(vertical)): 
        vertical[n] = [vertical[n][1], vertical[n][0]]

    toRemove.extend(vertical)
    toRemove.extend(horizontal)

    toRemove = removeDups(toRemove)

    for cords in toRemove: 
        gameMap[cords[0]][cords[1]] = "*"
        score += 1 

    return gameMap, score

# if __name__ == "__main__": 
#     score = 0 

#     gameMap = [
#         ["*", "b", "*", "*", "*"],
#         ["b", "b", "*", "b", "b"],
#         ["*", "b", "*", "*", "*"],
#         ["*", "b", "*", "*", "*"],
#         ["*", "*", "*", "*", "*"]
#     ]

#     toRemove = []

#     inverse = inverseMap(gameMap)
#     vertical = checkToRemove(inverse) 
#     horizontal = checkToRemove(gameMap)

#     for n in range(len(vertical)): 
#         vertical[n] = [vertical[n][1], vertical[n][0]]

#     toRemove.extend(vertical)
#     toRemove.extend(horizontal)

#     toRemove = removeDups(toRemove)

#     for cords in toRemove: 
#         gameMap[cords[0]][cords[1]] = "*"
#         score += 1 

#     print(gameMap)
#     print(score)

#     #remove does 