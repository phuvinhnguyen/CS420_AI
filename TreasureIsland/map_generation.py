import random
import re
class nmap:
    '''
    Item on the map:
▪ The map is divided into multi-regions
▪ Tiles contain labels:
• A tile with label r (r is an integer) is belong to r-th region.
o r = 0 is sea.
• A tile with label “M” is a part of a mountain.
• A tile with label “P” is a prison.
• A tile with label “T” is the treasure position.
'''
    maxnregion = 6
    Mrate = 0.2
    Prate = 0.05


    def __init__(self, input_dir=''):
        if input_dir == '': return
        
        with open(input_dir, 'r') as rf:
            data = rf.readlines()
            self.mapsize = [int(i) for i in data[0].split(' ')]
            self.turnnumber_pp = int(data[1])
            self.turnnumber_fr = int(data[2])
            self.nregion = int(data[3])
            self.Tx, self.Ty = [int(i) for i in data[4].split(' ')]
            
            self.mmap = []
            self.region = {}
            for i in range(self.nregion): self.region[i] = [[],[]]
            self.M = [[],[]]

            mask = '([0-9]+)'
            y_axis = 0
            for line in data[5:]:
                l = line[:-1].split(';')
                x_axis = 0
                for tile in l:
                    reg = int(re.findall(mask, tile)[0])
                    self.region[reg][1].append(x_axis)
                    self.region[reg][0].append(y_axis)
                    if 'M' in tile:
                        self.M[0].append(y_axis)
                        self.M[1].append(x_axis)
                        
                    x_axis += 1
                self.mmap.append(l)
                y_axis += 1

    def generate(self, size: int):
        '''
        generate new map to save to file, not to use directly
        '''
        self.mapsize = (size, size)
        self.turnnumber_pp = random.randint(2,4)
        self.turnnumber_fr = size
        self.mmap = [ ['0']*size for _ in range(size)]

        lsize = size - 1
        rregion = 1
        HP = False
        while lsize > 3:
            x,y,s = random.randint(0,size-1), random.randint(0,size-1), random.randint(2,lsize)
            lsize = s
            s = int(s/2)
            for n in range(max(x-s,0), min(size,x+s)):
                for m in range(max(y-s,0), min(size,y+s)):
                    self.mmap[n][m] = '%d' % (rregion)
                    mr, pr = random.randint(0,100)/100, random.randint(0,100)/100
                    if mr < self.Mrate:
                        self.mmap[n][m] += 'M'
                    if pr < self.Prate:
                        self.mmap[n][m] += 'P'
                        HP = True
            rregion += 1
        self.nregion = rregion

        if not HP:
            px,py = random.randint(0,size-1), random.randint(0,size-1)
            self.mmap[px][py] += 'P'

        self.Tx,self.Ty = random.randint(0,size-1), random.randint(0,size-1)
        self.mmap[self.Tx][self.Ty] += 'T'

    def save(self, filename:str):
        with open('./input/'+filename, 'w+') as wf:
            mmap = []
            for line in self.mmap:
                m = str(line)[1:-1].replace(', ', ';').replace('\'', '')+'\n'
                mmap.append(m)
            wf.writelines([str(self.mapsize[0])+' '+str(self.mapsize[1])+'\n',
                            str(self.turnnumber_pp)+'\n',
                            str(self.turnnumber_fr)+'\n',
                            str(self.nregion)+'\n',
                            str(self.Tx)+' '+str(self.Ty)+'\n'
                            ] + mmap)

    def map(self):
        return self.mmap

if __name__ == '__main__':
    mmap = nmap()
    mmap.generate(10)
    mmap.save('map64_1.txt')