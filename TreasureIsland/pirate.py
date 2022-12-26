import random
from map_generation import nmap

class pirate:
    #RULE
    '''
▪ At the beginning of the game, the pirate gives the agent a hint about
the treasure, the first hint is always true.
▪ At the beginning of each turn, the pirate gives the agent a hint about
the treasure, the hint requires verification to make sure it is real!
▪ After 2-4 turns, the pirate reveals the prison that he is staying in. (The
prison is randomly selected).
▪ After n turns (based on the map size), the pirate is free from the
prison and moves directly to the treasure (shortest path). The speed
of the pirate is upto 2 tiles each turn. If the pirate reaches the treasure
tile, the agent loses the game. -> LOSE
'''
    #HINT:
    '''
NOTE:
CMD IS THE INDEX OF THE HINT. EX: GIVE A HINT OF TYPE 1 => CMD=1
VERIFY: BOOLEAN, IF THAT HINT IS TRUE THEN VERIFY=TRUE, ELSE FALSE
X IS HORIZONTAL, Y IS VERTICAL

1. A list of random tiles that doesn't contain the treasure (1 to 12).
TODO: RETURN A LIST -> [CMD, VERIFY, [[LIST OF RANDOM TILES_X],[LIST OF RANDOM TILES_Y]]]
EACH RANDOM TILE: [X,Y]

2. 2-5 regions that 1 of them has the treasure.
TODO: [CMD, VERIFY, [REGIONS]]
REGION: 0,1,2,3,... CAN GET FROM MAP

3. 1-3 regions that do not contain the treasure.
TODO: [CMD, VERIFY, [REGIONS]]
REGION: 0,1,2,3,... CAN GET FROM MAP

4. A large rectangle area that has the treasure.
TODO: [CMD, VERIFY, [UPLEFT_X, UPLEFT_Y, DOWNRIGHT_X, DOWNRIGHT_Y]]

5. A small rectangle area that doesn't has the treasure.
TODO: [CMD, VERIFY, [UPLEFT_X, UPLEFT_Y, DOWNRIGHT_X, DOWNRIGHT_Y]]

6. He tells you that you are the nearest person to the treasure (between
you and the prison he is staying).
TODO: [CMD, VERIFY]

7. A column and/or a row that contain the treasure (rare).
TODO: [CMD, VERIFY, [ROW_INDEX, COLLUMN_INDEX]]
IF ROW_INDEX OR COLLUMN_INDEX IS -1 THEN THAT ROW, COLLUMN IS NOT CONSIDER(HOWEVER, AT LEAST ONE OF THEM != -1)

8. A column and/or a row that do not contain the treasure.
TODO: [CMD, VERIFY, [ROW_INDEX, COLLUMN_INDEX]]

9. 2 regions that the treasure is somewhere in their boundary.
TODO: [CMD, VERIFY, [REGIONS]]

10.The treasure is somewhere in a boundary of 2 regions.
TODO: [CMD, VERIFY]

11.The treasure is somewhere in an area bounded by 2-3 tiles from sea.
TODO: [CMD, VERIFY, No OF TILES]

12.A half of the map without treasure (rare).
TODO: [CMD, VERIFY, PART]
PART IN {UP, DOWN, LEFT, RIGHT}

13.From the center of the map/from the prison that he's staying, he tells
you a direction that has the treasure (W, E, N, S or SE, SW, NE, NW)
TODO: [CMD, VERIFY, PART]
PART IN 
(The shape of area when the hints are either W, E, N or S is triangle).
14.2 squares that are different in size, the small one is placed inside the
bigger one, the treasure is somewhere inside the gap between 2
squares. (rare)
15.The treasure is in a region that has mountain
'''
    def type1(m,n):
        verify = True
        s =  random.randint(1, 12)
        tileList = []
        for i in range(s):
            xs=random.randint(0,n)
            ys=random.randint(0,m)
            if (xs == tx and ys == ty):
                verify = False
            if [xs, ys] not in tileList:
                tileList.append([xs, ys])
            else:
                i = i - 1
        return [1,verify,tileList]

    '''2. 2-5 regions that 1 of them has the treasure.
    TODO: [CMD, VERIFY, [REGIONS]]
    REGION: 0,1,2,3,... CAN GET FROM MAP'''
    def type2(m,n):
        s = min(random.randint(2,5),r)
        regionList = []
        while (len(regionList)<s):
            x=random.randint(0,r-1);
            if x not in regionList:
                regionList.append(x)
        t = map[tx][ty].replace('T','')
        if (int(t) in regionList):
            return [2, True, regionList]
        else:
            return [2, False, regionList]

    def type3(m,n):
        s = min(random.randint(1,3),r)
        regionList = []
        while (len(regionList)<s):
            x=random.randint(0,r-1);
            if x not in regionList:
                regionList.append(x)
        t = map[tx][ty].replace('T','')
        if (int(t) in regionList):
            return [2, False, regionList]
        else:
            return [2, True, regionList]

    for i in range(5):
        print(type3(m,n))     

    def type4(m,n):
        l=int(random.randint(0,n))+1
        w=int(random.randint(0,m))+1
    
        xs=random.randint(0,n)
        ys=random.randint(0,m)
        xe=min(xs+l,n)
        ye=min(ys+w,m)
        
        for i in range(ys,ye+1):
            for j in range(xs,xe+1):
                if (map[i][j].find("T")!=-1):
                    return [4,True,[xs,ys,xe,ye]]
        return [4,False,[xs,ys,xe,ye]]

    def type5(m,n):
        l=int(random.randint(0,n)*0.3)+1
        w=int(random.randint(0,m)*0.3)+1
    
        xs=random.randint(0,n)
        ys=random.randint(0,m)
        xe=min(xs+l,n)
        ye=min(ys+w,m)
        
        for i in range(ys,ye+1):
            for j in range(xs,xe+1):
                if (map[i][j].find("T")!=-1):
                    return [5,False,[xs,ys,xe,ye]]
        return [5,True,[xs,ys,xe,ye]]

    def type7(m,n):
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,m)
            c=random.randint(-1,n)
        
        if (r==-1):
            for i in range(0,m+1):
                if (map[i][c].find("T")>-1):
                    return [7, True, [-1,c]]
            return [7, False, [-1,c]]
            
        if (c==-1):
            for i in range(0,n+1):
                if (map[r][i].find("T")>-1):
                    return [7, True, [r,-1]]
            return [7, False, [r,-1]]
        
        return [7,map[r][c].find("T")>-1,[r,c]]


    #MAIN FUNCTIONALITIES
    def __init__(self, mmap:nmap):
        self.map = mmap
        #choose randomly a position of prison and set it as init position of pirate 
        pass
    def hint(self):
        pass
    def report(self):
        #report present position
        pass
