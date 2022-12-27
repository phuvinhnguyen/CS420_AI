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
    map = [["0","0","4","4","4"],["0","1T","4M","4","4"],["1","1M","3M","3","5"],["2","1","1","3","5"],["2","2","0","3","5"]]
    m=len(map)-1
    n=len(map[0])-1
    r=6
    tx,ty=1,1

    def type1():
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

    def type2():
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

    def type3():
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

    def type4():
        l=int(random.randint(0,n))+1
        w=int(random.randint(0,m))+1

        xs=random.randint(0,n)
        ys=random.randint(0,m)
        xe=min(xs+l,n)
        ye=min(ys+w,m)

        return [4,(xs<=tx) and (tx<=xe) and (ys<=ty) and (ty<=ye),[xs,ys,xe,ye]]

    def type5():
        l=int(random.randint(0,n)*0.3)+1
        w=int(random.randint(0,m)*0.3)+1

        xs=random.randint(0,n)
        ys=random.randint(0,m)
        xe=min(xs+l,n)
        ye=min(ys+w,m)

        return [5,not ((xs<=tx) and (tx<=xe) and (ys<=ty) and (ty<=ye)),[xs,ys,xe,ye]]

    def type7():
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

    def type8():
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,m)
            c=random.randint(-1,n)

        if (r==-1):
            for i in range(0,m+1):
                if (map[i][c].find("T")>-1):
                    return [7, False, [-1,c]]
            return [7, True, [-1,c]]

        if (c==-1):
            for i in range(0,n+1):
                if (map[r][i].find("T")>-1):
                    return [7, False, [r,-1]]
            return [7, True, [r,-1]]

        return [7,map[r][c].find("T")==-1,[r,c]]

    #bound = have same edge or vertix
    def createBoundaryList():
        b = []
        t = map[tx][ty].translate({ord(i): None for i in 'MPT'})
        b.append(int(t))
        #if (map[max(tx-1,0)][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}) not in b):
        #    b.append(map[max(tx-1,0)][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}))
        if (map[max(tx-1,0)][ty].translate({ord(i): None for i in 'MPT'}) not in b):
           b.append(map[max(tx-1,0)][ty].translate({ord(i): None for i in 'MPT'}))
        #if (map[max(tx-1,0)][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}) not in b):
        #    b.append(map[max(tx-1,0)][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}))
        if (map[tx][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(map[max(tx-1,0)][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}))
        if (map[tx][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(map[max(tx-1,0)][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}))
        #if (map[min(tx+1,m)][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}) not in b):
        #    b.append(map[max(tx-1,0)][max(ty-1,0)].translate({ord(i): None for i in 'MPT'}))
        if (map[min(tx+1,m)][ty].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(map[max(tx-1,0)][ty].translate({ord(i): None for i in 'MPT'}))
        #if (map[min(tx+1,m)][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}) not in b):
        #    b.append(map[max(tx-1,0)][min(ty+1,n)].translate({ord(i): None for i in 'MPT'}))
        return b.remove(t);

    boundaryList = createBoundaryList()
    def type9():
        t = map[tx][ty].translate({ord(i): None for i in 'MPT'})
        x=-1
        y=-1
        while (x==y):
            x=random.randint(0,r)
            y=random.randint(0,r)
        if ((x==t) or (y==t)):
            if ((x+y-t) in boundaryList):
                return [9, True, [x,y]]
        return [9,False, [x,y]]

    def type10():
        return [10, len(boundaryList)>0]

    def type11():
        x=random.randint(1,3)
        for i in range(1,x+1):
            if (map[max(tx-i,0)][ty]=="0") or (map[min(tx+i,m)][ty]=="0") or (map[tx][max(ty-i,0)]=="0") or (map[tx][min(ty+i,n)]=="0"):
                return [11, True]
        return [11,False]

    def type12():
        x=random.randint(1,4)
        match x:
            case 1: #up
                return [12, tx <= int(m/2), "U"]
            case 2: #down
                return [12, tx >= int(m/2), "D"]
            case 3: #left
                return [12, ty <= int(n/2), "L"]
            case 4: #right
                return [12, ty >= int(n/2), "R"]

    def type13():
        x=random.randint(1,8)
        match x:
            case 1: #E
                return [13, ((m*tx-n*ty)>=0) and ((m*tx+n*ty-n*m)>=0), "E"]
            case 2: #N
                return [13, ((m*tx-n*ty)>=0) and ((m*tx+n*ty-n*m)<=0), "N"]
            case 3: #W
                return [13, ((m*tx-n*ty)<=0) and ((m*tx+n*ty-n*m)<=0), "W"]
            case 4: #S
                return [13, ((m*tx-n*ty)<=0) and ((m*tx+n*ty-n*m)>=0), "S"]
            case 5: #SE
                return [13, (tx >= int(m/2)) and (ty >= int(n/2)), "SE"]
            case 6: #EN
                return [13, (tx <= int(m/2)) and (ty >= int(n/2)), "NE"]
            case 7: #NW
                return [13, (tx <= int(m/2)) and (ty <= int(n/2)), "WS"]
            case 8: #WS
                return [13, (tx >= int(m/2)) and (ty <= int(n/2)), "WE"]

    def type14():
        bl=random.randint(3,n)
        bw=random.randint(3,m)

        bxs=random.randint(0,n-bl)
        bys=random.randint(0,m-bw)
        bxe=min(bxs+bl,n)
        bye=min(bys+bw,m)

        sl=random.randint(1,bxe-bxs-2)
        sw=random.randint(1,bye-bys-2)
        sxs=random.randint(bxs+1,bxe-1)
        sys=random.randint(bxs+1,bxe-1)
        sxe=min(sxs+sl,bxe-1)
        sye=min(sys+sw,bye-1)

        return [14,(((bxs<=tx) and (tx<=sxs)) or ((sxe<=tx) and (tx<=bxe))) and (((bys<=ty) and (ty<=sys)) or ((sye<=ty) and (ty<=bye))),[[bxs,bys,bxe,bye],[sxs,sys,sxe,sye]]]

    def type15():
        return [15,map[tx][ty].find("M")>-1]


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
