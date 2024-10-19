from Components.createMap import createMap
from Components.drawMap import drawMap
from Components.plotRandomVirus import plotRandomVirus
from Components.spawnBlock import spawnBlock
from Components.checkForActive import checkForActive
from Components.dropBlock import dropBlock
from Components.moveBlock import moveBlock, moveDown, rotateBlock
from Components.checkFourInRow import checkFourInRow

import time as t 
from pynput import keyboard
import os

# TODO:
# check four in a row 
# add a new block called f {color} -> falling blocks that cant be moved 
# make other blocks fall if a block breaks and its not attached to a virus

# TODO later: 
# code the start page into the code
# add death screen 
# fix rotate 
# clean code / add comments 


# * -> empty tile
# b -> blue 
# g -> green 
# r -> red 
# y -> yellow 
# v {color} -> virus with the specific color, ex: "v b" -> virus blue 
# a {color} -> block that is active and the colors, ex: "a g" -> active green block

# Global variables
gameMap = []

HEIGHT = 15
WIDTH = 15

def onPress(key):
    global gameMap, gameTime, level, score 

    if key == keyboard.Key.up:
        gameMap = rotateBlock(gameMap)
    elif key == keyboard.Key.down:
        gameMap = moveDown(gameMap)
    elif key == keyboard.Key.right:
        gameMap = moveBlock(gameMap, 1)
    elif key == keyboard.Key.left:
        gameMap = moveBlock(gameMap, -1)

    drawMap(gameMap, gameTime, level, score)

def clearConsole():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main(): 
    global gameMap, fastDrop, rotate, gameTime, level, score

    # start screen 

    # vars 
    gameSpeed = 1
    level = 1
    score = 0

    startTime = t.time()

    gameMap = plotRandomVirus(createMap(HEIGHT, WIDTH), level)

    listener = keyboard.Listener(on_press=onPress)
    listener.start()

    while True: 
        clearConsole()
        gameTime = int(t.time() - startTime)

        if checkForActive(gameMap) == False:
            gameMap = spawnBlock(gameMap) 
        else: 
            gameMap = dropBlock(gameMap)

        drawMap(gameMap, gameTime, level, score, mainLoop=True)

        gameMap, score = checkFourInRow(gameMap, score)
        t.sleep(gameSpeed)

main()