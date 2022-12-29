import pirate
from map_generation import nmap
from agent import agentkm,var
import random
import numpy as np

def get_init_place(mmap:nmap):
    m = var(mmap.mapsize, mmap.M[0]+mmap.region[0][0], mmap.M[1]+mmap.region[0][1], 0)
    pos = np.where(m.mask==1)
    sel = random.randint(0, len(pos[0])-1)
    return [pos[0][sel],pos[1][sel]]

if __name__ == '__main__':
    mmap = nmap('input/a.txt')
    pir = pirate.pirate(mmap)
    
    init_place = get_init_place(mmap) #generate initial place
    result = None

    agent = agentkm(init_place, mmap)

    while True:
        if agent.WIN == True:
            result = 'WIN'
            break
        elif pir.WIN == True:
            result = 'LOSE'
            break

        input = pir.hint()
        agent.step(input)

        agent_view = agent.mask
        agent_pos = agent.report()
        pirate_pos = pir.report()

        #display
    

    #show result