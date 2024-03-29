import random
import math
from map_generation import nmap
from agent import agentkm

class pirate:
    #RULE
    
#MAIN FUNCTIONALITIES
    def __init__(self, mmap:nmap):
        self.map = mmap
        self.mcountdown = mmap.turnnumber_fr
        #choose randomly a position of prison and set it as init position of pirate 
        listPrison = []
        for i in range (self.map.mapsize[0]):
            for j in range (self.map.mapsize[1]):
                if self.map.mmap[i][j].find("P") == True:
                    listPrison.append([i,j])
        self.posPirate = listPrison[random.randint(0,len(listPrison)-1)]
        self.region = mmap.nregion
        self.tx = mmap.Tx
        self.ty = mmap.Ty
        self.WIN = False
        self.posAgent = (-1,-1)
              
    def getAgenPos(self, agent:agentkm):
        self.posAgent = agent.pos

    def createBoundaryList(self):
        b = []
        t = self.map.mmap[self.tx][self.ty].translate({ord(i): None for i in 'MPT'})
        b.append(int(t))
        if (self.map.mmap[max(self.tx-1,0)][self.ty].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(self.map.mmap[max(self.tx-1,0)][self.ty].translate({ord(i): None for i in 'MPT'}))

        if (self.map.mmap[self.tx][max(self.ty-1,0)].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(self.map.mmap[max(self.tx-1,0)][max(self.ty-1,0)].translate({ord(i): None for i in 'MPT'}))

        if (self.map.mmap[self.tx][min(self.ty+1,self.map.mapsize[1] - 1)].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(self.map.mmap[max(self.tx-1,0)][min(self.ty+1,self.map.mapsize[1] - 1)].translate({ord(i): None for i in 'MPT'}))

        if (self.map.mmap[min(self.tx+1,self.map.mapsize[0] - 1)][self.ty].translate({ord(i): None for i in 'MPT'}) not in b):
            b.append(self.map.mmap[max(self.tx-1,0)][self.ty].translate({ord(i): None for i in 'MPT'}))

        b = list(filter((t).__ne__, b))
        b = list(filter((int(t)).__ne__, b))

        return b

    def type1(self):
        verify = True
        s =  random.randint(1, 12)
        tileList = []
        x_list = []
        y_list = []
        for i in range(s):
            xs=random.randint(0,self.map.mapsize[1] - 1)
            ys=random.randint(0,self.map.mapsize[0] - 1)
            if (xs == self.tx and ys == self.ty):
                verify = False
            if [xs, ys] not in tileList:
                tileList.append([xs, ys])
                x_list.append(xs)
                y_list.append(ys)
            else:
                i = i - 1
        return [1,verify,[x_list,y_list]]
    
    def type2(self):
        s = min(random.randint(2,5), self.region)
        regionList = []
        while (len(regionList)<s):
            x=random.randint(0, self.region - 1)
            if x not in regionList:
                regionList.append(x)
        t = self.map.mmap[self.tx][self.ty][0]
        if (int(t[0]) in regionList):
            return [2, True, regionList]
        else:
            return [2, False, regionList]

    def type3(self):
        s = min(random.randint(1,3), self.region)
        regionList = []
        while (len(regionList)<s):
            x=random.randint(0,self.region - 1)
            if x not in regionList:
                regionList.append(x)
        t = self.map.mmap[self.tx][self.ty].replace('T','')
        if (int(t[0]) in regionList):
            return [3, False, regionList]
        else:
            return [3, True, regionList]

    def type4(self):
        l=int(random.randint(0,self.map.mapsize[1] - 1)) + 1
        w=int(random.randint(0,self.map.mapsize[0] - 1)) + 1
    
        xs=random.randint(0,self.map.mapsize[1] - 1)
        ys=random.randint(0,self.map.mapsize[0] - 1)
        xe=min(xs+l,self.map.mapsize[1] - 1)
        ye=min(ys+w,self.map.mapsize[0] - 1)
        
        return [4,(xs <= self.tx) and (self.tx <=xe) and (ys <= self.ty) and (self.ty <= ye),[xs,ys,xe,ye]]

    def type5(self):
        l=int(random.randint(0,self.map.mapsize[1] - 1)*0.3)+1
        w=int(random.randint(0,self.map.mapsize[0] - 1)*0.3)+1
    
        xs=random.randint(0,self.map.mapsize[1] - 1)
        ys=random.randint(0,self.map.mapsize[0] - 1)
        xe=min(xs+l,self.map.mapsize[0] - 1)
        ye=min(ys+w,self.map.mapsize[0] - 1)
        
        return [5,not ((xs <= self.tx) and (self.tx <= xe) and (ys <= self.ty) and (self.ty <=ye)),[xs,ys,xe,ye]]

    def type6(self): #passing position of agent
        xAgent, yAgent = self.posAgent[0], self.posAgent[1]
        disPirate = (abs(self.posPirate[0] - self.tx) + abs(self.posPirate[1] - self.ty))
        disAgent = (abs(xAgent - self.tx) + abs(yAgent - self.ty))
        return [6,disAgent < disPirate]

    def type7(self):
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,self.map.mapsize[0] - 1)
            c=random.randint(-1,self.map.mapsize[1] - 1)
        
        if (r==-1):
            for i in range(0,self.map.mapsize[0]):
                if (self.map.mmap[i][c].find("T")>-1):
                    return [7, True, [-1,c]]
            return [7, False, [-1,c]]
            
        if (c==-1):
            for i in range(0,self.map.mapsize[1]):
                if (self.map.mmap[r][i].find("T")>-1):
                    return [7, True, [r,-1]]
            return [7, False, [r,-1]]
        
        return [7,self.map.mmap[r][c].find("T")>-1,[r,c]]

    def type8(self):
        r=-1
        c=-1
        while ((r==-1) and (c==-1)):
            r=random.randint(-1,self.map.mapsize[0] - 1)
            c=random.randint(-1,self.map.mapsize[1] - 1)
        
        if (r==-1):
            for i in range(0,self.map.mapsize[0]):
                if (self.map.mmap[i][c].find("T")>-1):
                    return [7, False, [-1,c]]
            return [8, True, [-1,c]]
            
        if (c==-1):
            for i in range(0,self.map.mapsize[1]):
                if (self.map.mmap[r][i].find("T")>-1):
                    return [7, False, [r,-1]]
            return [8, True, [r,-1]]
        
        return [8,self.map.mmap[r][c].find("T")==-1,[r,c]]

    def type9(self):
        boundaryList = self.createBoundaryList()
        t = self.map.mmap[self.tx][self.ty].translate({ord(i): None for i in 'MPT'})
        x=-1
        y=-1
        while (x==y):
            x=random.randint(0,self.region-1)
            y=random.randint(0,self.region-1)
        if ((x==t) or (y==t)):
            if ((x+y-t) in boundaryList):
                return [9, True, [x,y]]
        return [9,False, [x,y]]

    def type10(self):
        boundaryList = self.createBoundaryList()
        return [10, len(boundaryList)>0]

    def type11(self):
        x=random.randint(1,3)
        for i in range(1,x+1):
            if (((self.map.mmap[max(self.tx-i,0)][self.ty]=="0") or 
                (self.map.mmap[min(self.tx+i,self.map.mapsize[0] - 1)][self.ty]=="0") or 
                (self.map.mmap[self.tx][max(self.ty-i,0)]=="0") or 
                (self.map.mmap[self.tx][min(self.ty+i,self.map.mapsize[1] - 1)]=="0")) and
                '0' not in self.map.mmap[self.tx][self.ty]):
                return [11, True]
        return [11,False]

    def type12(self):
        x=random.randint(1,4)
        match x:
            case 1: #up
                return [12, self.tx <= int((self.map.mapsize[0] - 1)/2), "U"]
            case 2: #down
                return [12, self.tx >= int((self.map.mapsize[0] - 1)/2), "D"]
            case 3: #left
                return [12, self.ty <= int((self.map.mapsize[1] - 1)/2), "L"]
            case 4: #right
                return [12, self.ty >= int((self.map.mapsize[1] - 1)/2), "R"]

    def type13(self):
        x=random.randint(1,8)
        match x:
            case 1: #E
                return [13, self.ty-int(self.map.mapsize[1]/2) >= 0 and (abs(self.tx-int(self.map.mapsize[0]/2))/max(abs(self.ty-int(self.map.mapsize[1]/2))*1.0,0.001)) < 1, "E"]
            case 2: #N
                return [13, self.tx-int(self.map.mapsize[0]/2) < 0 and (abs(self.ty-int(self.map.mapsize[1]/2))/max(abs(self.tx-int(self.map.mapsize[0]/2))*1.0,0.001)) < 1, "N"]
            case 3: #W
                return [13, self.ty-int(self.map.mapsize[1]/2) < 0 and (abs(self.tx-int(self.map.mapsize[0]/2))/max(abs(self.ty-int(self.map.mapsize[1]/2))*1.0,0.001)) < 1, "W"]
            case 4: #S
                return [13, self.tx-int(self.map.mapsize[0]/2) >= 0 and (abs(self.ty-int(self.map.mapsize[1]/2))/max(abs(self.tx-int(self.map.mapsize[0]/2))*1.0,0.001)) < 1, "S"]
            case 5: #SE
                return [13, (self.tx >= int((self.map.mapsize[0])/2)) and (self.ty >= int((self.map.mapsize[1])/2)), "SE"]
            case 6: #EN
                return [13, (self.tx < int((self.map.mapsize[0])/2)) and (self.ty >= int((self.map.mapsize[1])/2)), "NE"]
            case 7: #NW
                return [13, (self.tx < int((self.map.mapsize[0])/2)) and (self.ty < int((self.map.mapsize[1])/2)), "WS"]
            case 8: #WS
                return [13, (self.tx >= int((self.map.mapsize[0])/2)) and (self.ty < int((self.map.mapsize[1])/2)), "WE"]

    def type14(self):
        bl=random.randint(3,(self.map.mapsize[1] - 1))
        bw=random.randint(3,(self.map.mapsize[0] - 1))
    
        bxs=random.randint(0,(self.map.mapsize[1] - 1)-bl)
        bys=random.randint(0,(self.map.mapsize[0] - 1)-bw)
        bxe=min(bxs+bl,(self.map.mapsize[1] - 1))
        bye=min(bys+bw,(self.map.mapsize[0] - 1))

        sl=random.randint(1,bxe-bxs-2)
        sw=random.randint(1,bye-bys-2)
        sxs=random.randint(bxs+1,bxe-1)
        sys=random.randint(bxs+1,bxe-1)
        sxe=min(sxs+sl,bxe-1)
        sye=min(sys+sw,bye-1)
        
        return [14,
        (((bxs<=self.tx) and (self.tx<=sxs)) or ((sxe<=self.tx) and (self.tx<=bxe))) and (((bys<=self.ty) and (self.ty<=sys)) or ((sye<=self.ty) and (self.ty<=bye))),
        [[sxs,sys],[sxe,sye]],[[bxs,bys],[bxe,bye]]]

    def type15(self):
        return [15,self.map.mmap[self.tx][self.ty].find("M")>-1]
    
    def pirateMove(self):
        xM,yM = self.tx-self.posPirate[0], self.ty-self.posPirate[1]
        if xM != 0:
            self.posPirate[0] += (2-abs(xM)%2) * (-1 if xM < 0 else 1)
        elif yM != 0:
            self.posPirate[1] += (2-abs(yM)%2) * (-1 if yM < 0 else 1)
        if xM == 0 and yM == 0:
            self.WIN = True

        # xMove, yMove = int((self.tx-self.posPirate[0])/(abs(self.tx-self.posPirate[0]))), int((self.ty-self.posPirate[1])/(abs(self.ty-self.posPirate[1])))
        # if (xMove==0) or (yMove==0):
        #     if (self.posPirate[0]+xMove==self.tx) and (self.posPirate[1]+yMove==self.ty):
        #         self.posPirate[0]+=xMove
        #         self.posPirate[1]+=2*yMove
        #     else:
        #         self.posPirate[0]+=2*xMove
        #         self.posPirate[1]+=2*yMove
        # else:
        #     self.posPirate[0]+=xMove
        #     self.posPirate[1]+=yMove
    
        # if (self.tx - self.posPirate[0] == 0):
        #     xMove = 0
        # else :
        #     xMove = int((self.tx-self.posPirate[0])/(abs(self.tx-self.posPirate[0])))

        # if (self.ty - self.posPirate[1] == 0):
        #     yMove = 0
        # else :
        #     yMove = int((self.ty-self.posPirate[1])/(abs(self.ty-self.posPirate[1])))
            
        # if (xMove==0) or (yMove==0):
        #     if (self.posPirate[0]+xMove==self.tx) and (self.posPirate[1]+yMove==self.ty):
        #         self.posPirate[0]+=xMove
        #         self.posPirate[1]+=2*yMove
        #     else:
        #         self.posPirate[0]+=2*xMove
        #         self.posPirate[1]+=2*yMove
        # else:
        #     self.posPirate[0]+=xMove
        #     self.posPirate[1]+=yMove
        
        # if self.posPirate[0] == self.tx and self.posPirate[1] == self.ty:
        #     self.WIN = True
            
    def hint(self, type):
        if self.mcountdown != 0:
            self.mcountdown -= 1
        else:
            self.pirateMove()

        h = []
        while(True):
            x = int(random.random()*1000)
            if x<=75:
                h = self.type1()
            elif x<=150:
                h = self.type2()
            elif x<=225:
                h = self.type3()
            elif x<=300:
                h = self.type4()
            elif x<=375:
                h = self.type5()
            elif x<=450:
                h = self.type6()
            elif x<=480:
                h = self.type7()
            elif x<=555:
                h = self.type8()
            elif x<=630:
                h = self.type9()
            elif x<=705:
                h = self.type10()
            elif x<=780:
                h = self.type11()
            elif x<=810:
                h = self.type12()
            elif x<=885:
                h = self.type13()
            elif x<=960:
                h = self.type14()
            else:
                h = self.type15()
            if (h[1]==True) or type == 0:
                break
        return h
    def report(self):
        #report present position
        return self.posPirate
if __name__ == '__main__':
    pir = pirate(nmap('./input/a.txt'))
    print('this is map: nmap.mmap')
    print(pir.map.mmap)
    print('this is mapsize: nmap.mapsize')
    print(pir.map.mapsize)
    print('this is pos of Treasure')
    print(pir.map.Tx, pir.map.Ty)
