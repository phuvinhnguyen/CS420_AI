import random
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
            for line in data[5:]:
                l = line.split(';')
                self.mmap.append(l)

    def generate(self, size: int):
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
                        self.mmap[n][m] += ',M'
                    if pr < self.Prate:
                        self.mmap[n][m] += ',P'
                        HP = True
            rregion += 1
        self.nregion = rregion

        if not HP:
            px,py = random.randint(0,size-1), random.randint(0,size-1)
            self.mmap[py][px] += ',P'

        self.Tx,self.Ty = random.randint(0,size-1), random.randint(0,size-1)
        self.mmap[self.Ty][self.Tx] += ',T'

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