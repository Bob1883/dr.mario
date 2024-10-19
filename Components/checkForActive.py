def checkForActive(gameMap:list) -> bool: 
    for i in range(len(gameMap)): 
        for j in range(len(gameMap[0])): 
            if "a" in gameMap[i][j]: 
                return True 
            
    return False


# if __name__ == "__main__":
#     gameMap = [
#         ["*", "b", "b", "*", "*"],
#         ["*", "v b", "v b", "*", "*"],
#         ["*", "*", "*", "*", "*"],
#         ["*", "b", "r", "*", "*"],
#         ["*", "*", "*", "*", "*"],
#     ]

#     print(checkForActive(gameMap))