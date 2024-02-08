
from mcpi.minecraft import Minecraft
import mcpi.minecraft as Minecraft , mcpi.block as block , time , random

mc = Minecraft.Minecraft.create()

def get_chunks(x,z): # multiple chunk scan
    x,z = x//16 *16,z//16 *16 # absolute chunk base coordinates (16 base)
    raw_data = [];categ_data = [];indiv_data = [];height_data = [];indexes = [];suit_pos = [];bad_indexes = []
    
    h = mc.getHeight(x,z)
    mc.setBlock(x,h,z,1) #trace abs-base coordinate position of the chunk where player is located

    x,z = int(x-64),int(z-64) #tune for perfect 9x9 chunk scan
    for k in range(0,0+129,16): #loop each chunk start on x-line
        for l in range(0,0+129,16): #loop each chunk start on z-line
            for j in range(k,k+16,4): #loop individual blocks of sel. chunk on x-line
                for i in range(l,l+16,4): #loop individual blocks of sel. chunk on z-line
                    h = mc.getHeight(x+i,z+j)
                    #mc.setBlock(x+i,h,z+j,5) # optional trace data with filling scanned blocks
                    if(mc.getBlock(x+i,h,z+j)==18 or 161):
                        h = h - 4
                    raw_data.append(h)
                    #mc.setBlock(x+i,h,z+j,5) # optional trace data with filling scanned blocks
    
    
    # the 4 for functions categorise data to be used under certain categories
    for i in range(81):categ_data.append([]) # create spec array for 81 categorized sublists
    for i in range(len(raw_data)): # add data from raw to partitioned list
        part = i//16
        categ_data[part].append(raw_data[i])
    for i in categ_data: # add calculated values to a spec list
        minn = min(i)
        maxx = max(i)
        diff = abs(minn-maxx)
        indiv_data.append([minn,maxx,diff])
    for i in range(81): height_data.append(indiv_data[i][2]) # make a list solely for height differences

    
    
    
    iter = -1
    while len(indexes) < 8 and iter < 64: # the whole while function gathers the best chunks with lowest height difference, and removes the ones that are too close by
        iter += 1
        bad_indexes = []
        ext = []
        tmp = []

        for i in range(len(height_data)): # add next layer of lowest height diff chunks
            if height_data[i] == iter:
                ext.append(i)
        indexes.extend(ext)

        for i in range(1,len(indexes) - 1): # record indexes of chunk locations that are too close
            if i not in bad_indexes:
                for j in range(len(indexes) - 1):
                    if (indexes[j] == indexes[i] + 1 or indexes[j] == indexes[i] + 9 or 
                    indexes[j] == indexes[i] + 10 or
                    indexes[j] == indexes[i] + 2 or indexes[j] == indexes[i] + 18) and indexes[j] != indexes[i]: # modified for best randomizer possibility
                        bad_indexes.append(j)

        for i in range(len(indexes)): # filter the bad indexes for same 'indexes' array
            if (i not in bad_indexes):
                tmp.append(indexes[i])
        indexes = tmp



    # randomise for beter suitable location coordinates
    random.shuffle(indexes)
    random.shuffle(indexes)
    random.shuffle(indexes)


    for i in indexes: # record coord values for other modules to use from the return statement
        suit_pos.append([x + i%9*16,z + i//9*16])


    # for i in suit_pos: # optional trace of best chunks selected
    #     mc.setBlocks(i[0],0,i[1],i[0],128,i[1],1)
    
    # for the terraforming using the above data done by Jabbar
    # i will be getting the average height of a chunk then appending that into the array intialized bellow
    averageHeightData = []

    # for loop to append data in to the loop
    for row in categ_data:
        print(row)
        averageHeightData.append([(sum(row)/len(row))])
    
    #averageChunkHeight. if the program scans 16 and we know its 144 x 144
    print()
    print()
    print(averageHeightData)
    #editing values such that we round the values so the blocks are evenly distributed by using the round method and turning floats to ints to avoid any future type issues 
    #counts through each list in AverageHeightData and returns the first value for each list 
    for count in range(0,81): 
        averageHeightData[count][0] = int(round(averageHeightData[count][0],0))
        print(averageHeightData[count][0])

    print()

    chunkChangeAverage = []
    arrSquare = [-1,1,-9,9]
    elementsCounted = 1 
    #ChunkChange Average used to find out the change in height that each chunk will go through and
    #elementsCounted simple counter
    #arrSquare a list used to find the adjacent chunks to the chunk being compared.

    #for loop will go through each chunk height data and then through each element in arrSquare adding the average of the average height of the 
    # chunk compared to and the average height of the adjacent chunks 
    for count in range(0,81):
        averageHeight  = averageHeightData[count][0]
        for element in arrSquare:
            if(count + element > 80 or count + element < 0):
                continue
            else:
                elementsCounted +=1
                averageHeight = averageHeight + averageHeightData[count + element][0]
        
        chunkChangeAverage.append([round(averageHeight/elementsCounted,0)])
        averageHeight = 0
        elementsCounted = 1
	
    print(len(chunkChangeAverage))

    for items in chunkChangeAverage:
        print(items)

    count = 0
   
   
             

    #GET BIOME SOIL such that when we level the area of the chunk the facing blocks wont be representive of the biome 
    xnew,ynew,znew = mc.player.getPos()
    soil = mc.getBlock(xnew,mc.getHeight(xnew,znew),znew)

    for k in range(0,0+129,16): #loop each chunk start on x-line
        for l in range(0,0+129,16): #loop each chunk start on z-line
            if(l != 0):
                count += 1
            for j in range(k,k+16,4): #loop individual blocks of sel. chunk on x-line
                for i in range(l,l+16,4): #loop individual blocks of sel. chunk on z-line
                    if(j == k+16-4 and i == l+16-4):
                        print("here")
                        mc.setBlocks(x+i-12,chunkChangeAverage[count][0]+2,z+j-12-4+4+3-3, x+i+3,chunkChangeAverage[count][0] + 14,z+j+4-1,0) # clear the chunks
                        mc.setBlocks(x+i-12,chunkChangeAverage[count][0]+2,z+j-12-4+4+3-3, x+i+3,chunkChangeAverage[count][0]+2,z+j+4-1,soil) # set the soil of the ground to be the same of the biome 

    return suit_pos




if __name__ == "__main__":
    start_time = time.time()

    x,y,z = mc.player.getPos()

    best_pos = get_chunks(x,z)

    print("--- %s seconds ---" % (time.time() - start_time))

    
