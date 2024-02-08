from mcpi.minecraft import Minecraft
import mcpi.minecraft as Minecraft , mcpi.block as block , time , random

import chunk
import road

mc = Minecraft.Minecraft.create()

if __name__ == "__main__":
    x, y, z = mc.player.getPos()
    print('\nstarting...')
    mc.postToChat('starting...')

    chunkList = []
    print('\nfinding chunks...')
    mc.postToChat('finding chunks...')
    chunkList = chunk.get_chunks(x,z)
    print('done')
    mc.postToChat('done')

    print('\ngetting front door coordinates...')
    mc.postToChat('getting front door coordinates...')
    road.roadStart()
    print('done')
    mc.postToChat('done')

