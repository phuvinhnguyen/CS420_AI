import pirate
from map_generation import nmap
from agent import agentkm,var
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio.v3 as iio
import copy
import hint_verification
from hint_verification import hintVerify


def displayText(map,view):
    #fig = plt.figure()
    # Function to show the heat map
    v = view.copy()
    for i in range(len(v)):
        for j in range(len(v[0])):
            v[i][j]=data[i][j]*view[i][j]

    fig, ax = plt.subplots(figsize = (16,5))
    im = ax.imshow(v)
    for i in range(len(v)):
        for j in range(len(v[0])):
            texts[i][j].remove()
            texts[i][j] = ax.text(j, i, map[i][j],ha="center", va="center", color="w")
            
    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close()
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
    mmap = nmap("input/map32_0.txt")
    pir = pirate.pirate(mmap)
    maps = [] #lưu giá trị các bước di chuyễn
    agent_views = []
    init_place = get_init_place(mmap) #generate initial place
    result = None
    rpp = mmap.turnnumber_pp
    logs = []
    turn = 0
    agent = agentkm(init_place, mmap)

    while True:
        turn +=1
        log = []
        log.append(turn)
        
        agent_prev_pos = agent.report()
        pir.getAgenPos(agent)
        pirate_prev_pos = pir.report()
        input = pir.hint(turn==1)
        #action return 'move','scan','move and scan'
        action = agent.step(input)
        agent_view = copy.deepcopy(agent.mask.mask)
        log.append("Hint "+str(turn)+": "+hintVerify(input))
        # position of pirate
        if rpp > 0:
            rpp -= 1
        else:
            agent.pirate_pos = pir.posPirate
            if rpp ==0:
                log.append('Pirate revealed that he stays at '+str(pir.posPirate))
            else: 
                log.append('Pirate move to '+str(pir.posPirate))
            rpp -=1
        #print(input)
        #print(agent_view)

        agent_views.append(agent_view)
        agent_pos = agent.report()
        pirate_pos = pir.report()
        log.append("Agent vefity hint: "+str(input[1]))
        if (action=="move"):
            log.append("Agent move to "+str(agent_pos))
        elif (action=="move and scan"):
            log.append("Agent move to "+str(agent_pos)+" and small scan")
        else:
            log.append("Agent make a big scan")
        map=copy.deepcopy(mmap.mmap)
        updateMap(agent_pos[0],agent_pos[1],"A",map)
        updateMap(pirate_pos[0],pirate_pos[1],"Pr",map)
        maps.append(map)
        logs.append(log)

        if agent.WIN == True:
            result = 'WIN'
            break
        elif pir.WIN == True:
            result = 'LOSE'
            break
    
    with open('output/o.txt', '+w') as wf:
        #for map, agen_view in zip(maps, agent_views):
        #    for line in map:
        #        wf.write(str(line)+'\n')
        #    wf.write('\n')
        #    for line in agent_view:
        #        wf.write(str(line)+'\n')
        #   wf.write('-----------------------------------\n')
        wf.write(str(len(logs))+'\n')
        wf.write(result+'\n')

        for i in logs:
            wf.write("Turn "+str(i[0])+'\n')
            for j in range(1,len(i)):
                wf.write(i[j]+'\n')
            wf.write('\n')

    #print(logs)
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
    iio.imwrite("./move.gif", [displayText(maps[i],agent_views[i]) for i in range(len(maps))], duration=1000)
