import random
from map_generation import nmap

class pirate:
    #RULE
    map = [["0","0","4P","4","4"],["0","1T","4M","4","4"],["1","1M","3M","3P","5"],["2","1","1","3","5"],["2","2","0","3","5P"]]
    m=len(map)-1
    n=len(map[0])-1
    r=6
    tx,ty=1,1
    
    def piratePosition():
        listPrison = []
        for i in range (m+1):
            for j in range (n+1):
                if map[i][j].find("P") == True:
                    listPrison.append([i,j])
        x = random.randint(0,len(listPrison)-1)
        return listPrison[x][0], listPrison[x][1]
    
    xPirate, yPirate = piratePosition()
    
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

    def type6(xAgent, yAgent): #passing position of agent
        disPirate = math.sqrt((xPirate - tx)**2 + (yPirate - ty)**2)
        disAgent = math.sqrt((xAgent - tx)**2 + (yAgent - ty)**2)
        return [6,disAgent > disPirate]

    def type7():
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,m)
            c=random.randint(-1,n)

        return [7,(tx==c) or (ty==r),[r,c]]

    def type8():
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,m)
            c=random.randint(-1,n)

        return [7,(tx!=c) and (ty!=r),[r,c]]

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
        if (t in b):
            return b.remove(t)
        else:
            return b

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
        for i in range(2,4):
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
        self.pos
        #choose randomly a position of prison and set it as init position of pirate 
        pass
    def hint(self):
        pass
    def report(self):
        #report present position
        return 
        pass
