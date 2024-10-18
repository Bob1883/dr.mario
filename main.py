import time as t 
from Components.createMap import createMap
from Components.drawMap import drawMap
from Components.plotRandomVirus import plotRandomVirus

# * -> empty tile
# b -> blue 
# g -> green 
# r -> red 
# y -> yellow 
# v {color} -> virus with the specific color, ex: "v b" -> virus blue 
# a {color} -> block that is active and the colors, ex: "a g" -> active green block

HEIGHT = 15
WIDTH = 15

def main(): 
    # start screen 

    # vars 
    gameSpeed = 0.1 
    level = 5
    
    score = 0
    startTime = t.time()

    gameMap = plotRandomVirus(createMap(HEIGHT, WIDTH), level)

    while True: 
        gameTime = int(t.time() - startTime)
        drawMap(gameMap, gameTime, level, score)
        t.sleep(1)

main()