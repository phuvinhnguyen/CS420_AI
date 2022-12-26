import numpy as np
from map_generation import nmap
from Astart import a_star_graph_search

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
    def get_goal_function(self, des):
        def dest(cell):
            return cell == des
        return dest
    def get_successor_function(self, grid):
        def get_clear_adjacent_cells(cell):
            i, j = cell
            return (
                (i + a, j + b)
                for a in (-1, 0, 1)
                for b in (-1, 0, 1)
                if a != 0 or b != 0
                if 0 <= i + a < len(grid)
                if 0 <= j + b < len(grid[0])
                if grid[i + a][j + b] == 0
            )
        return get_clear_adjacent_cells
    def get_heuristic(self, grid, des):
        M, N = len(grid), len(grid[0])
        (a, b) = des
        def get_clear_path_distance_from_goal(cell):
            (i, j) = cell
            return max(abs(a - i), abs(b - j))
        return get_clear_path_distance_from_goal

    #MAIN FUNCTIONALITIES
    def __init__(self, init_place:list, map_size:list, map:nmap):
        self.pos = init_place #[x,y]
        self.mask = var(map_size)
        self.tele = True
        self.map = map
        self.logic = []
        self.pirate_pos = [-map_size,-map_size]
        self.mapsize = map_size
        self.grid = [[1 if 'M' in x else 0 for x in y] for y in map.mmap]
    
    
    def score(self, size=1):
        return np.array([np.sum(self.mask[max(0,i-size):min(self.mapsizep[1],i+size+1),max(0,j-size):min(self.mapsizep[0],j+size+1)]) for i in range(self.mapsize[1]) for j in range(self.mapsize[0])]).reshape((self.mapsize[1],self.mapsize[0]))
    
    
    def step(self, input):
        self.solveI(input)
        m = self.score()
        #find des
        des = np.where(m == np.max(m))
        des = (des[0][0],des[1][0])
        #find path to des
        path = a_star_graph_search(self.pos,
                                    goal_function=self.get_goal_function(des),
                                    successor_function=self.get_successor_function(self.grid),
                                    heuristic= self.get_heuristic(self.grid, des))[:5]

        if path == None:
            if self.tele == True:
                self.tele == False
                self.pos = des
            self.scan(len(path))
            return
        for i in path:
            self.mask.mask[i[1],i[0]] = 1 if 'T' in self.map.mmap[i[1]][i[0]] else 0
        self.scan(len(path))


    def scan(self, typ:int):
        xb,xe,yb,ye
        if typ == 0:
            xb,xe = max(0,self.pos[0]-2),min(self.pos[0]+3,self.mapsize[0])
            yb,ye = max(self.pos[1]-2,0),min(self.pos[1]+3,self.mapsize[1])
        elif typ <= 2:
            xb,xe = max(0,self.pos[0]-1),min(self.pos[0]+2,self.mapsize[0])
            yb,ye = max(self.pos[1]-1,0),min(self.pos[1]+2,self.mapsize[1])
        elif typ <= 4:
            return
        
        for x in range(xb,xe):
            for y in range(yb,ye):
                self.mask.mask[y,x] = 1 if 'T' in self.map.mmap[y][x] else 0

        
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
