import random
from map_generation import nmap

class pirate:
    #RULE
    
#MAIN FUNCTIONALITIES
    def __init__(self, mmap:nmap):
        self.map = mmap
        m = self.map.mapsize[0]
        n = self.map.mapsize[1]
        #choose randomly a position of prison and set it as init position of pirate 
        listPrison = []
        for i in range (m):
            for j in range (n):
                if self.map.mmap[i][j].find("P") == True:
                    listPrison.append([i,j])
        x = random.randint(0,len(listPrison)-1)
        return listPrison[x]
        pass
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