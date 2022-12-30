import random
from map_generation import nmap
from agent import agentkm

class pirate:
    #RULE
    
#MAIN FUNCTIONALITIES
    def __init__(self, mmap:nmap, agent:agentkm):
        self.map = mmap
        #choose randomly a position of prison and set it as init position of pirate 
        listPrison = []
        for i in range (self.map.mapsize[0]):
            for j in range (self.map.mapsize[1]):
                if self.map.mmap[i][j].find("P") == True:
                    listPrison.append([i,j])
        self.posPirate = listPrison[random.randint(0,len(listPrison)-1)]
        self.region = mmap.nregion
    def hint(self):
        pass
    def report(self):
        #report present position
        pass
if __name__ == '__main__':
    pir = pirate(nmap('./input/a.txt'))
    print('this is map: nmap.mmap')
    print(pir.map.mmap)
    print('this is mapsize: nmap.mapsize')
    print(pir.map.mapsize)
    print('this is pos of Treasure')
    print(pir.map.Tx, pir.map.Ty)