from mcpi.minecraft import Minecraft
import mcpi.minecraft as Minecraft , mcpi.block as block , time
import random, math

mc = Minecraft.Minecraft.create()

def house(x, y, z, l, w):
    storeys = random.randint(1, 3)
    for i in range(0, storeys): # builds the walls and floors of the house
        height = y-1
        height += (i*4) # increments by 4 to build cubes higher and higher
        mc.setBlocks(x-(w/2), height, z, x+(w/2), height+4, z+l, block.WOOD_PLANKS.id, plankRand) # create a cube of blocks
        mc.setBlocks(x-(w/2)+1, height+1, z+1, x+(w/2)-1, height+3, z+l-1, 0) # makes it hollow 
    
    subdivisions(x, y, z, l, w, storeys)
    glowstone(x, y, z, l, w, storeys)
    stairs(x, y, z, w, storeys)
    roofs(x, y, z, l, w, storeys)
    windows(x, y, z, l, w, storeys)
    houseDeco(x, y, z, l, w, storeys)
    ladder(x, y, z, l, w, storeys)

    if (w+1) % 2 == 0: # if the width of the house is even, create another door
        mc.setBlocks(x-1, y, z, x+2, y+2, z, 95, glassRand)
        mc.setBlock(x+1, y+1, z, doorRand, 8)
        mc.setBlock(x+1, y, z, doorRand, 6)
        mc.setBlock(x+1, y+2, z-1, 50, 4) # torch above door
    else: 
        mc.setBlocks(x-1, y, z, x+1, y+2, z, 95, glassRand)

    doors(x, y+1, z)

def windows(x, y, z, l, w, storeys):
    buildWindows = random.randint(1, 1)
    if(buildWindows == 1):
        leftsidewidthOfWindows = random.randint(2,math.floor((w - 3)/2))
        heightOfWindows = 2
        height = 0
        while height < ((storeys * 3) + 1):
            if (height == 0 or height == 3 or height == 6 or height == 7):
                        height = height + 1
                        continue
            else:
                if (heightOfWindows != 2):
                    if(mc.getBlock(x+1,height - 1,z+1)== 20):
                        height = height + 1
                        continue
                    else:
                        if(random.randint(0,5) != 1):
                            for width in range(2,leftsidewidthOfWindows+2):
                                mc.setBlock(x+width,y+height,z, 20)
                        if(random.randint(0,5) != 1):
                            for width in range(1,leftsidewidthOfWindows + 1):
                                mc.setBlock(x-width -1,y+height,z, 20)
                else:
                    if (random.randint(0,5) != 1):
                        for width in range(2,leftsidewidthOfWindows+2):
                            mc.setBlock(x+width,y+height,z, 20)
                    if (random.randint(0,5) != 1):
                        for width in range(1,leftsidewidthOfWindows + 1):
                            mc.setBlock(x-width - 1,y+height,z, 20)
            height = height + 1

def stairs(x, y, z, w, storeys):
    if storeys > 1: # stairs forward
        for i in range(0, 4):
            mc.setBlocks(x+(w/2)-1, y+(i), z+2+(i), x+(w/2)-2, y+(i), z+2+(i), stairRand, 2) # loop to create stairs going up
        mc.setBlocks(x+(w/2)-1, y+3, z+1, x+(w/2)-2, y+3, z+4, 0) # creates space for stairs
    if storeys > 2: # stairs backward
        for i in range(0, 4):
            mc.setBlocks(x+(w/2)-3, y+4+(i), z+4-(i), x+(w/2)-4, y+4+(i), z+4-(i), stairRand, 3) # loop to create stairs going up, backwards
        mc.setBlocks(x+(w/2)-3, y+7, z+2, x+(w/2)-4, y+7, z+4, 0) # creates space for stairs

def subdivisions(x, y, z, l, w, storeys):
    if l > 15:
        long = 2
    else: 
        long = 0
    height = y
    height += ((storeys-1)*4)
    doorX = random.choice([1, 2, w-2, w-3]) # randomizes placement of door to the room 
    wallX = random.randint(2, w-4)
    entranceZ = random.randint(0, 2)
    if storeys >= 1:
        if storeys == 1: # picks a number of rooms
            rooms = random.choice([1, 2]) 
        else:
            rooms = random.randint(1, 3) 
        if rooms >= 1:
            mc.setBlocks(x-(w/2)+1, height, z+l/2+2-long, x+(w/2)-1, height+2, z+l/2+2-long, block.WOOD_PLANKS.id, wallRand) # create a wall of blocks
            doors(x-(w/2)+doorX, height+1, z+l/2+2-long)
        if rooms > 1:
            mc.setBlocks(x-(w/2)+1+wallX, height, z+l/2+2-long, x-(w/2)+1+wallX, height+2, z+l-1, block.WOOD_PLANKS.id, wallRand) # create a wall of blocks
            mc.setBlocks(x-(w/2)+1+wallX, height, z+l*0.75+2-long, x-(w/2)+1+wallX, height+1, z+l*0.75+entranceZ-long, 0) # create a entrance
            mc.setBlock(x-(w/2)+1+wallX, height+2, z+l*0.75+entranceZ-long, block.GLOWSTONE_BLOCK.id)
        if rooms > 2:
            mc.setBlocks(x-1, height, z+1, x-1, height+2, z+l/2+2-long-1, block.WOOD_PLANKS.id, wallRand)
            mc.setBlocks(x-1, height, z+4, x-1, height+1, z+2+entranceZ, 0) # create a entrance
            mc.setBlock(x-1, height+2, z+2+entranceZ, block.GLOWSTONE_BLOCK.id)
        subdivisions(x, y, z, l, w, storeys-1)
        #mc.postToChat('Floor {}: {} room'.format(storeys, rooms))

def doors(x, y, z):
    mc.setBlock(x, y, z, doorRand, 8) # spawn top half of door 
    mc.setBlock(x, y-1, z, doorRand, 1) # bottom half
    mc.setBlock(x, y+1, z-1, 50, 4) # torch above door

def roofs(x, y, z, l, w, storeys):
    y += (storeys-1)*4
    mc.setBlocks(x-(w/2), y+4, z, x+(w/2), y+10, z+l, 0) # clear space for the attic
    roofType = random.choice(['rectangle', 'triangle']) #randomly selects a type of roof
    if roofType == 'rectangle': # RECTANGLE ROOF
        mc.setBlocks(x-1, y+2+math.ceil(w/2), z+math.ceil(w/2)-1, x+1, y+math.ceil(w/2)+2, z+l-math.ceil(w/2)+1, 95, glassRand) # fill the top with planks
        for i in range(0, math.ceil(w/2)):
            mc.setBlocks(x-(w/2)+i, y+3+i, z-1+i, x+(w/2)-i, y+3+i, z-1+i, stairRand, 2) # front side
            mc.setBlocks(x-(w/2)-1+i, y+3+i, z+i-1, x-(w/2)-1+i, y+3+i, z+l-i+1, stairRand, 0) # right side
            mc.setBlocks(x+(w/2)+1-i, y+3+i, z+i-1, x+(w/2)+1-i, y+3+i, z+l-i+1, stairRand, 1) # left side
            mc.setBlocks(x-(w/2)+i, y+3+i, z+l-i+1, x+(w/2)-i, y+3+i, z+l-i+1, stairRand, 3) # back side
    else:             # TRIANGLE ROOF
        for i in range (0, math.ceil(w/2)+1):
            mc.setBlocks(x-(w/2)+i, y+3+i, z, x+(w/2)-i, y+3+i, z, block.WOOD_PLANKS.id, plankRand) # front side
            mc.setBlocks(x-(w/2)+i, y+3+i, z+l, x+(w/2)-i, y+3+i, z+l, block.WOOD_PLANKS.id, plankRand) # back side
            mc.setBlocks(x-(w/2)+i-1, y+3+i, z-1, x-(w/2)+i-1, y+3+i, z+l+1, stairRand, 0) # right side
            mc.setBlocks(x+(w/2)-i+1, y+3+i, z-1, x+(w/2)-i+1, y+3+i, z+l+1, stairRand, 1) # left side
        if (w+1) % 2 != 0:
            mc.setBlocks(x, y+8, z-1, x, y+8, z+l+1, 95, glassRand) # fill the top with glass
    
def houseDeco(x, y, z, l, w, storeys):
    for i in range(0, storeys): # builds random log pillars in house corners
        height = y-1
        height += (i*4) # increments by 4 to build a storey higher
        mc.setBlocks(x-(w/2), height, z, x-(w/2), height+4, z, block.WOOD.id, logRand)
        mc.setBlocks(x+(w/2), height, z, x+(w/2), height+4, z, block.WOOD.id, logRand)
        mc.setBlocks(x-(w/2), height, z+l, x-(w/2), height+4, z+l, block.WOOD.id, logRand)
        mc.setBlocks(x+(w/2), height, z+l, x+(w/2), height+4, z+l, block.WOOD.id, logRand)
    
    if storeys == 3: # builds balcony if 3 storeys
        for i in range(0, 3):   
            mc.setBlocks(x-(w/2)+2+i, y+7-i, z-1, x+(w/2)-2-i, y+7-i, z-3+i, block.WOOD_PLANKS.id, plankRand)
        
        mc.setBlocks(x-(w/2)+2, y+8, z-1, x+(w/2)-2, y+8, z-3, fenceRand) # balcony rails
        mc.setBlocks(x-(w/2)+3, y+8, z-1, x+(w/2)-3, y+8, z-2, 0)

        if (w+1) % 2 == 0: # entrance to balcony
            mc.setBlocks(x-1, y+8, z, x+2, y+10, z, 95, glassRand)
            mc.setBlocks(x+1, y+8, z, x+1, y+9, z, 0) 
        else:
            mc.setBlocks(x-1, y+8, z, x+1, y+10, z, 95, glassRand)
        mc.setBlocks(x, y+8, z, x, y+9, z, 0)
    
    mc.setBlock(x-(w/2)+1, y, z+l-1, block.BED.id, 8)
    mc.setBlock(x-(w/2)+1, y, z+l-2, block.BED.id)

    mc.setBlock(x+(w/2)-1, y, z+l-1, block.BED.id, 8)
    mc.setBlock(x+(w/2)-1, y, z+l-2, block.BED.id)

    mc.setBlock(x+(w/2)-1, y+4, z+l-1, block.BED.id, 8)
    mc.setBlock(x+(w/2)-1, y+4, z+l-2, block.BED.id)

    mc.setBlock(x-(w/2)+1, y+4, z+l-1, block.BED.id, 8)
    mc.setBlock(x-(w/2)+1, y+4, z+l-2, block.BED.id)
    
    mc.setBlocks(x-(w/2)+1, y+2, z+l-1, x-(w/2)+1, y+2, z+l-2, block.BOOKSHELF.id)
    mc.setBlocks(x+(w/2)-1, y+2, z+l-1, x+(w/2)-1, y+2, z+l-2, block.BOOKSHELF.id)
    if storeys > 1:
        mc.setBlocks(x-(w/2)+1, y, z+2, x-(w/2)+1, y+2, z+l/2, block.BOOKSHELF.id)
        mc.setBlocks(x-(w/2)+1, y+4, z+2, x-(w/2)+1, y+6, z+l/2, block.BOOKSHELF.id)
        mc.setBlocks(x+(w/2)-1, y+6, z+l-1, x+(w/2)-1, y+6, z+l-2, block.BOOKSHELF.id)
        mc.setBlocks(x-(w/2)+1, y+6, z+l-1, x-(w/2)+1, y+6, z+l-2, block.BOOKSHELF.id)
    if storeys > 2:
        mc.setBlock(x+(w/2)-1, y+8, z+l-1, block.BED.id, 8)
        mc.setBlock(x+(w/2)-1, y+8, z+l-2, block.BED.id)

        mc.setBlock(x-(w/2)+1, y+8, z+l-1, block.BED.id, 8)
        mc.setBlock(x-(w/2)+1, y+8, z+l-2, block.BED.id)

def glowstone(x, y, z, l, w, storeys): # places a random number of glowstones per floor
    lights = random.randint(2, 4) # picks a number of lights
    height = y-1
    height += (storeys*4)
    if storeys >= 1:
        for i in range(0, lights):
            lightX = random.randint(1, w-1)
            lightZ = random.randint(0, l-2)
            mc.setBlock(x-(w/2)+lightX, height, z+1+lightZ, block.GLOWSTONE_BLOCK.id)
        glowstone(x, y, z, l, w, storeys-1)

def ladder(x, y, z, l, w, storeys): # builds a ladder to the attic
    height = y
    height += ((storeys-1)*4)
    ladderX = random.randint(2, int(w/2-2))
    ladderZ = random.randint(2, int(l/2)-2)
    mc.setBlocks(x-(w/2)+ladderX, height, z+ladderZ, x-(w/2)+ladderX, height+3, z+ladderZ, 65) # randomized ladder placement
      
def start(x,y,z):
    global glassRand 
    glassRand = random.randint(1, 15)
    global stairList 
    stairList = [53, 67, 108, 109, 114, 128, 134, 135, 136, 156, 163, 164, 180, 203] # variety of different stairs
    global stairRand 
    stairRand = stairList[random.randint(0, 13)] # picks stairs for the house randomly
    global doorList 
    doorList = [193, 194, 195, 196, 197] # variety of different doors
    global doorRand 
    doorRand = doorList[random.randint(0, 4)] # picks doors for the house randomly
    global plankRand 
    plankRand = random.randint(0, 5) # picks a type of wood plank
    global wallRand 
    wallRand = random.randint(0, 5)
    global logRand 
    logRand = random.randint(0, 3) # picks a type of log
    global fenceList 
    fenceList = [113, 188, 189, 190, 191, 192] # variety of different stairs
    global fenceRand 
    fenceRand = fenceList[random.randint(0, 5)] # picks stairs for the house randomly
    global l 
    l = random.randint(10, 18)
    global w 
    w = random.randint(8, 12)
    
    house(x,y,z+1,l,w)