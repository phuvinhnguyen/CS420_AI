import pirate
from map_generation import nmap
from agent import agentkm,var
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio.v3 as iio
import copy


def displayText(map):
    for i in range(len(data)):
        for j in range(len(data[0])):
            texts[i][j].remove()
            texts[i][j] = ax.text(j, i, map[i][j],ha="center", va="center", color="w")
            
    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image

def updateMap(z,t,k,map):
    map[z][t] += k
    
def get_init_place(mmap:nmap):
    m = var(mmap.mapsize, mmap.M[0]+mmap.region[0][0], mmap.M[1]+mmap.region[0][1], 0)
    while True:
        pos = np.where(m.mask==1)
        sel = random.randint(0, len(pos[0])-1)
        if 'P' not in mmap.mmap[pos[0][sel]][pos[1][sel]]:
            return [pos[0][sel],pos[1][sel]]

if __name__ == '__main__':
    mmap = nmap("input/map64_1.txt")
    pir = pirate.pirate(mmap)
    maps = [] #lưu giá trị các bước di chuyễn
    agent_views = []
    init_place = get_init_place(mmap) #generate initial place
    result = None
    rpp = mmap.turnnumber_pp
    
    agent = agentkm(init_place, mmap)

    while True:
        # position of pirate
        if rpp > 0:
            rpp -= 1
        else:
            agent.pirate_pos = pir.posPirate

        if agent.WIN == True:
            result = 'WIN'
            break
        elif pir.WIN == True:
            result = 'LOSE'
            break
            

        agent_prev_pos = agent.report()
        pir.getAgenPos(agent)
        pirate_prev_pos = pir.report()
        input = pir.hint()
        agent.step(input)
        agent_view = copy.deepcopy(agent.mask.mask)

        #print(input)
        #print(agent_view)

        agent_views.append(agent_view)
        agent_pos = agent.report()
        pirate_pos = pir.report()
        map=copy.deepcopy(mmap.mmap)
        updateMap(agent_pos[0],agent_pos[1],"A",map)
        updateMap(pirate_pos[0],pirate_pos[1],"Pr",map)
        maps.append(map)
    
    with open('output/o.txt', '+w') as wf:
        for map, agen_view in zip(maps, agent_views):
            for line in map:
                wf.write(str(line)+'\n')
            wf.write('\n')
            for line in agent_view:
                wf.write(str(line)+'\n')
            wf.write('-----------------------------------\n')
        wf.write(result)

    #print(maps[0])
    #show result
    # Generating data for the heat map
    data = []
    for i in range(len(map)):
        d=[]
        for j in range(len(map[0])):
             t=mmap.mmap[i][j]
             d.append(int(t.translate({ord(k): None for k in 'MPT'})))
        data.append(d)
    print(data)
                  
    fig = plt.figure()
    # Function to show the heat map
    fig, ax = plt.subplots()
    im = ax.imshow(data)
    #fig.tight_layout()
    #plt.show()
    texts=[]
    for i in range(len(data)):
        text=[]
        for j in range(len(data[0])):
           text.append(ax.text(j, i, "0",ha="center", va="center", color="w"))
        texts.append(text)
    ims=[]
    kwargs_write = {'fps':1.0, 'quantizer':'nq'}
    iio.imwrite("./move.gif", [displayText(i) for i in maps], duration=1000)
