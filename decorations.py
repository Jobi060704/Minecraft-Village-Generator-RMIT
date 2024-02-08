from mcpi.minecraft import Minecraft
import mcpi.minecraft as Minecraft , mcpi.block as block , time
import random

mc = Minecraft.Minecraft.create()

def streetLight(x,y,z):
    y += 1
    if x < 0:
        x = x - 4
    # lamp post
    else :
        x = x + 4
    mc.setBlocks(x,y,z,x,y+3,z,85)
    # lamp
    mc.setBlock(x,y+4,z,89)
    mc.setBlock(x-1,y+4,z,96,6)
    mc.setBlock(x+1,y+4,z,96,7)
    mc.setBlock(x,y+4,z-1,96,4)
    mc.setBlock(x,y+4,z+1,96,5)
    mc.setBlock(x,y+5,z,96,2)

def tree(x,y,z):
    if x < 0:
        x = x - 4
    # lamp post
    else :
        x = x + 4
    # leaves
    randLeaves = random.randint(0,1)
    if randLeaves == 0:
        leafChoice = random.randint(0,3)
        mc.setBlocks(x-1,y+3,z-1,x+1,y+6,z+1,18, leafChoice)
        mc.setBlocks(x-2,y+4,z-1,x+2,y+5,z+1,18, leafChoice)
        mc.setBlocks(x-1,y+4,z-2,x+1,y+5,z+2,18, leafChoice)
    else:
        leafChoice = random.randint(0,3)
        mc.setBlocks(x-1,y+3,z-1,x+1,y+6,z+1,161, leafChoice)
        mc.setBlocks(x-2,y+4,z-1,x+2,y+5,z+1,161, leafChoice)
        mc.setBlocks(x-1,y+4,z-2,x+1,y+5,z+2,161, leafChoice)
    
    # logs
    randLogs = random.randint(0,1)
    if randLogs == 0:
        mc.setBlocks(x,y,z,x,y+4,z, 17, random.randint(0,3))
    else:
        mc.setBlocks(x,y,z,x,y+4,z, 162, random.randint(0,1))

def fencingSection(x,y,z):
    
    mc.setBlock(x,y,z,85)
    mc.setBlock(x,y+1,z,50, 5)


def start(xPos,yPos,zPos):
    
    if(random.randint(0,1) == 1):
        #left = True 
        xPos = xPos - 3

    else:
        #right = True
        xPos = xPos + 3

    randDecorations = random.randint(1,2)
    if(randDecorations == 1):
        streetLight(xPos,yPos,zPos)

    elif(randDecorations == 2):
        tree(xPos,yPos,zPos)


