import numpy as np
from map_generation import nmap

class var:
    def __init__(self, size:list, x_no:list=[], y_no:list=[], tr: bool=False) -> None:
        '''
        tr: true->input is pos of treasure
        '''
        if tr:
            self.mask = np.zeros((size[1],size[0]), dtype=np.int0)
            self.mask[x_no, y_no] = 1
        else:
            self.mask = np.ones((size[1],size[0]), dtype=np.int0)
            self.mask[x_no, y_no] = 0
    def __mul__(self, x):
        re = var((1,1))
        re.mask = self.mask&x.mask
        return re
    def __add__(self, x):
        re = var((1,1))
        re.mask = self.mask|x.mask
        return re


class agentkm:
    #RULE
    '''
▪ Initial stage: spawn at a random tile EXCEPT sea (“0” tile), prison
(tile with label “P”) and mountain (tile with label “M”)
▪ Each turn:
• The agent has 2 action each turn, the available action:
o Verification, verify a hint is a truth or a liar.
o Move straight 1-2 steps in a direction then perform a
small scan.
o Move straight 3-4 steps in a direction.
o Stay and perform a large scan.
• ONCE per game: the agent can teleport (instantly move to a
tile anywhere on the map EXCEPT tiles with label ”0”, and
“M”).
• The agent can not move to tile with label “0” and “M”.
• If the agent scans an area containing the treasure, the agent
wins the game. -> WIN.
'''
    #MAIN FUNCTIONALITIES
    def __init__(self, init_place:list, map_size:list, map:nmap):
        self.pos = init_place
        self.mask = var(map_size)
        self.map = map
        self.logic = []
        self.pirate_pos = [-map_size,-map_size]
        self.mapsize = map_size
    def step(self, map, info):
        
        pass
    def scan(self, map, pos:list, typ:str):
        pass
    def solveI(self, input):
        match input[0]:
            case 1: #1. A list of random tiles that doesn't contain the treasure (1 to 12).
                bmap = var(self.mapsize, [x for x in input[2][0]],[y for y in input[2][1]], not input[1])
                self.mask = self.mask*bmap
            case 2: #2. 2-5 regions that 1 of them has the treasure.
                bmap = var(self.mapsize,[],[],1)
                for i in input[2]:
                    bmap = bmap + var(self.mapsize, self.map.region[i][0], self.map.region[i][1], input[1])
                self.mask = self.mask*bmap  
            case 3: #3. 1-3 regions that do not contain the treasure.
                bmap = var(self.mapsize,[],[],1)
                for i in input[2]:
                    bmap = bmap + var(self.mapsize, self.map.region[i][0], self.map.region[i][1], not input[1])
                self.mask = self.mask*bmap 
            case 4: #4. A large rectangle area that has the treasure.
                bmap
                if input[1]:
                    bmap = var(self.mapsize,[],[],1)
                    bmap.mask[input[1]:input[3]+1,input[0]:input[2]] = 1
                else:
                    bmap = var(self.mapsize,[],[],0)
                    bmap.mask[input[1]:input[3]+1,input[0]:input[2]] = 0
                self.mask = self.mask*bmap
            case 5: #5. A small rectangle area that doesn't has the treasure.
                bmap
                if not input[1]:
                    bmap = var(self.mapsize,[],[],1)
                    bmap.mask[input[2][1]:input[2][3]+1,input[2][0]:input[2][2]] = 1
                else:
                    bmap = var(self.mapsize,[],[],0)
                    bmap.mask[input[2][1]:input[2][3]+1,input[2][0]:input[2][2]] = 0
                self.mask = self.mask*bmap
            case 6: #6. He tells you that you are the nearest person to the treasure (between you and the prison he is staying).
                x_ = -self.pirate_pos[1]+self.pos[1]
                y_ = self.pirate_pos[0]-self.pos[0]
                r_ = (x_*(self.pirate_pos[0]+self.pos[0])+y_*(self.pirate_pos[1]+self.pos[1]))/2
                bmap

                if x_ == 0 and y_ == 0:
                    return
                elif x_ == 0:
                    bmap = var(self.mapsize,[],[],1)
                    y = int(r_/y_)
                    if self.pos[1]-y > 0:
                        bmap.mask[y:,:] = 1
                    else:
                        bmap.mask[0:y+1,:] = 1
                elif y_ == 0:
                    bmap = var(self.mapsize,[],[],1)
                    x = int(r_/x_)
                    if self.pos[1]-x > 0:
                        bmap.mask[x:,:] = 1
                    else:
                        bmap.mask[0:x+1,:] = 1
                else:
                    bmap = var(self.mapsize,[],[],1)
                    for x in range(self.mapsize[1]):
                        y = int((r_ - x*x_)/y_)
                        bmap.mask[y:,x] = 1
                    if bmap.mask[self.pos[1], self.pos[0]] == 0:
                        bmap.mask = 1 - bmap.mask
                
                if not input[1]:
                    bmap.mask = 1 - bmap.mask
                self.mask = self.mask*bmap
            case 7: #7. A column and/or a row that contain the treasure (rare).
                bmap
                if input[2][0] == -1:
                    bmap = var(self.mapsize,[],[],1)
                    bmap.mask[:,input[2][1]] = 1
                elif input[2][1] == -1:
                    bmap = var(self.mapsize,[],[],1)
                    bmap.mask[input[2][0],:] = 1
                else:
                    bmap = var(self.mapsize,[],[],1)
                    bmap.mask[input[2][0],input[2][1]] = 1
                bmap.mask = 1-bmap.mask if not input[1] else bmap
                self.mask = self.mask*bmap
            case 8:
                if input[1]:
                    pass
                else:
                    pass
            case 9:
                if input[1]:
                    pass
                else:
                    pass
            case 10:
                if input[1]:
                    pass
                else:
                    pass
            case 11:
                if input[1]:
                    pass
                else:
                    pass
            case 12:
                if input[1]:
                    pass
                else:
                    pass
            case 13:
                if input[1]:
                    pass
                else:
                    pass
            case 14:
                if input[1]:
                    pass
                else:
                    pass
            case 15:
                if input[1]:
                    pass
                else:
                    pass
    def report(self):
        pass

# class agent:
#     #RULE
#     '''
# ▪ Initial stage: spawn at a random tile EXCEPT sea (“0” tile), prison
# (tile with label “P”) and mountain (tile with label “M”)
# ▪ Each turn:
# • The agent has 2 action each turn, the available action:
# o Verification, verify a hint is a truth or a liar.
# o Move straight 1-2 steps in a direction then perform a
# small scan.
# o Move straight 3-4 steps in a direction.
# o Stay and perform a large scan.
# • ONCE per game: the agent can teleport (instantly move to a
# tile anywhere on the map EXCEPT tiles with label ”0”, and
# “M”).
# • The agent can not move to tile with label “0” and “M”.
# • If the agent scans an area containing the treasure, the agent
# wins the game. -> WIN.
# '''
#     #MAIN FUNCTIONALITIES
#     def __init__(self, init_place:list(int, int), map_size:list(int, int)):
#         self.pos = init_place[:]
#         self.mask = var([],[],0,map_size)
#         self.ultra_instinct_map = var([],[],0,map_size)
#         self.logic = []
#         self.mapsize = map_size
#     def step(self, map, info):
#         pass
#     def scan(self, map, pos:list(int,int), typ:str):
#         pass
#     def solveI(self, input):
#         match input[0]:
#             case 1: #1. A list of random tiles that doesn't contain the treasure (1 to 12).
#                 bmap = var([x for x in input[2][:][0]],[y for y in input[2][:][1]],not input[1], self.mapsize)
#                 self.mask = self.mask*bmap
#                 self.ultra_instinct_map = self.ultra_instinct_map*bmap
#             case 2: #2. 2-5 regions that 1 of them has the treasure.

#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 3:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 4:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 5:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 6:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 7:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 8:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 9:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 10:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 11:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 12:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 13:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 14:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#             case 15:
#                 if input[1]:
#                     pass
#                 else:
#                     pass
#         pass
#     def report(self):
#         pass

if __name__ == '__main__':
    mmap = nmap('input/a.txt')
    a = agentkm((0,0),(8,8),mmap)
    a.solveI([1,True,[[1,2,4],[3,5,2]]])
    a.solveI([1,False,[[1,3,6,5,6],[3,2,3,5,2]]])
    print(a.mask.mask)
