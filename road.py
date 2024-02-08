from mcpi.minecraft import Minecraft

import mcpi.minecraft as Minecraft
import random, math
import decorations
import house

mc = Minecraft.Minecraft.create()
#this class will be used to build and save the x,y,z positions by using getters and setters when needed throughout the program 
# the class also contains the build method which will use the house.py start method to build houses on each of the x,y,z positions 
class HouseBuilding:
	def set_xPos(self,xPos):
		self.xPos = xPos
	
	def set_yPos(self,yPos):
		self.yPos = yPos
	
	def set_zPos(self,zPos):
		self.zPos = zPos
	
	def get_xPos(self):
		return self.xPos
	
	def get_yPos(self):
		return self.yPos
	
	def get_zPos(self):
		return self.zPos

	def buildHouses(self):
		#just call the house.py and passthrought x,y and z positions for it to build on
		house.start(self.xPos,self.yPos+1,self.zPos)

# def pointToPoint(xHouseCoord, zHouseCoord, x, z):
# 	width = xHouseCoord - x
# 	length = zHouseCoord - z

# 	# house pos
# 	mc.setBlock(xHouseCoord, zHouseCoord, 5)

# 	# if width negative
# 	if width < 0:
# 		for i in range(abs(width)+1):
# 			mc.setBlock(x-i,mc.getHeight(x,z),z, 4)
# 			xEndPoint = x-i
# 	else:
# 		for i in range(abs(width)+1):
# 			mc.setBlock(x+i,mc.getHeight(x,z),z, 4)
# 			xEndPoint = x+i
	
# 	# if length negative
# 	if length < 0:
# 		for j in range(abs(length)):
# 			mc.setBlock(xEndPoint,mc.getHeight(x,z),z-j, 4)
			
# 	else:
# 		for j in range(abs(length)):
# 			mc.setBlock(xEndPoint,mc.getHeight(x,z),z+j, 4)

def randomBlocks():
	blocks = [4,98,1]

	randomBlock = random.randint(0,2)
	return blocks[randomBlock]

def adjCalc(angle, hypotenuse):
	# adj = hypotenuse * cos()

	adj = hypotenuse * (math.cos(math.radians(angle)))
	return adj

def pathBranches(endPoint1, endPoint2, houseBuildingArray, direction):
	# pick path lengths for branches
	pathLength1 = random.randint(20,40)
	pathLength2 = random.randint(20,40)
	pathLength3 = random.randint(20,40)

	if direction == 1:
		# pick angle for branch
		angle = random.randint(25,65)
		for i in range(0,pathLength1):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1+length
			z = endPoint2+i
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength1 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)

				houseBuildingArray.append(house)
			 
		for i in range(0,pathLength1):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1+length
			z = endPoint2-i
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength1 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)

				houseBuildingArray.append(house)

	elif direction == 2:
		# pick angle for branch
		angle = random.randint(25,65)
		for i in range(0,pathLength2):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1+i
			z = endPoint2+length
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength2 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)

				houseBuildingArray.append(house)
		
		angle = random.randint(45,85)
		for i in range(0,pathLength2):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1-i
			z = endPoint2+length
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength2 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)
				
				houseBuildingArray.append(house)
			
	elif direction == 3:
		# pick angle for branch
		angle = random.randint(25,65)
		for i in range(0,pathLength3):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1-length
			z = endPoint2+i
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength3 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)

				houseBuildingArray.append(house)
		
		for i in range(0,pathLength3):
			# for each block on adjacent, find corresponding point on hypotenuse
			length = adjCalc(angle, i)
			x = endPoint1-length
			z = endPoint2-i
			y = mc.getHeight(x,z)

			# create 3-wide path on point
			mc.setBlock(x-1,y,z, randomBlocks())
			mc.setBlock(x,y,z, randomBlocks())
			mc.setBlock(x+1,y,z, randomBlocks())

			# once path is done store coordinates to place house later
			if(i == pathLength3 - 1):
				house = HouseBuilding()
				house.set_xPos(x+1)
				house.set_zPos(z)
				yPosHouse = mc.getHeight(x+1,z)
				house.set_yPos(yPosHouse)

				houseBuildingArray.append(house)

	return x, z, houseBuildingArray

def path(x, z, houseBuildingArray):
	# pick path lengths for starting path
	pathLength1 = random.randint(15,30)
	pathLength2 = random.randint(15,30)
	pathLength3 = random.randint(15,30)

	# pick angle for branch
	angle = random.randint(15,75)
	# create first path (north east)
	countFenceTimer = 0
	for i in range(0, pathLength1):
		# for each block on adjacent, find corresponding point on hypotenuse
		length = adjCalc(angle, i)
		xpos = x+length
		zpos = z-i
		y = mc.getHeight(xpos,zpos)

		# create 3-wide path on point
		mc.setBlock(xpos-1,y,zpos, randomBlocks())
		mc.setBlock(xpos,y,zpos, randomBlocks())
		mc.setBlock(xpos+1,y,zpos, randomBlocks())

		endPoint1 = xpos
		endPoint2 = zpos+1
		
		if(random.randint(1,12) == 5):
			ypos = mc.getHeight(xpos,zpos)
			decorations.start(xpos,ypos,zpos)

		if(countFenceTimer ==  5):

			if(random.randint(0,1) == 1):
				#left = True 
				xpos = xpos - 2
			else:
				#right = True
				xpos = xpos + 2

			yPos = mc.getHeight(xpos,zpos)
			decorations.fencingSection(xpos,yPos+1,zpos)

			countFenceTimer = 0
		countFenceTimer += 1

	
	# create first path branches
	direction = 1
	for i in range(0,2):
		# create angled path with fork
		endPoint1, endPoint2, houseBuildingArray = pathBranches(endPoint1, endPoint2, houseBuildingArray, direction)

	# pick angle for branch
	angle = random.randint(25,65)
	# create second path (south east)
	for i in range(0, pathLength2):
		# for each block on adjacent, find corresponding point on hypotenuse
		length = adjCalc(angle, i)
		xpos = x+length
		zpos = z+i
		y = mc.getHeight(xpos,zpos)

		# create 3-wide path on point
		mc.setBlock(xpos-1,y,zpos, randomBlocks())
		mc.setBlock(xpos,y,zpos, randomBlocks())
		mc.setBlock(xpos+1,y,zpos, randomBlocks())

		endPoint1 = xpos
		endPoint2 = zpos+1
		if(random.randint(1,12) == 5):
			ypos = mc.getHeight(xpos,zpos)
			decorations.start(xpos,ypos,zpos)

		if(countFenceTimer ==  5):

			if(random.randint(0,1) == 1):
				#left = True 
				xpos = xpos - 2
			else:
				#right = True
				xpos = xpos + 2

			yPos = mc.getHeight(xpos,zpos)
			decorations.fencingSection(xpos,yPos+1,zpos)

			countFenceTimer = 0
		countFenceTimer += 1

	# create second path branches
	direction = 2
	for i in range(0,2):
		# create angled path with fork
		endPoint1, endPoint2, houseBuildingArray = pathBranches(endPoint1, endPoint2, houseBuildingArray, direction)

	# pick angle for branch
	angle = random.randint(25,65)
	# create third path (west)
	for i in range(0, pathLength3):
		# for each block on adjacent, find corresponding point on hypotenuse
		length = adjCalc(angle, i)
		xpos = x-length-2
		zpos = z-i
		y = mc.getHeight(xpos,zpos)

		# create 3-wide path on point
		mc.setBlock(xpos-1,y,zpos, randomBlocks())
		mc.setBlock(xpos,y,zpos, randomBlocks())
		mc.setBlock(xpos+1,y,zpos, randomBlocks())

		endPoint1 = xpos
		endPoint2 = zpos+1

		if(random.randint(1,12) == 5):
			ypos = mc.getHeight(xpos,zpos)
			decorations.start(xpos,ypos,zpos)


		if(countFenceTimer ==  5):

			if(random.randint(0,1) == 1):
				#left = True 
				xpos = xpos - 2
			else:
				#right = True
				xpos = xpos + 2

			yPos = mc.getHeight(xpos,zpos)
			decorations.fencingSection(xpos,yPos+1,zpos)

			countFenceTimer = 0
		countFenceTimer += 1

	# create third path branches
	direction = 3
	for i in range(0,2):
		# create angled path with fork
		endPoint1, endPoint2, houseBuildingArray = pathBranches(endPoint1, endPoint2, houseBuildingArray, direction)
		
	return houseBuildingArray

def roadStart():
	x,y,z = mc.player.getPos()
	#this array will be used to store the objects of the house class and used to save x,y,z positions used later to loop through
	houseBuildingArray = []
	
	houseBuildingArray = path(x,z,houseBuildingArray)
	#houses array used to get each of the objects inside and call the buildhouse method in the house class
	for houses in houseBuildingArray: 
		houses.buildHouses()
