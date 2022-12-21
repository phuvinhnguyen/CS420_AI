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
TODO: RETURN A LIST -> [CMD, VERIFY, [LIST OF RANDOM TILES]]
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


9. 2 regions that the treasure is somewhere in their boundary.
10.The treasure is somewhere in a boundary of 2 regions.
11.The treasure is somewhere in an area bounded by 2-3 tiles from sea.
12.A half of the map without treasure (rare).
13.From the center of the map/from the prison that he's staying, he tells
you a direction that has the treasure (W, E, N, S or SE, SW, NE, NW)
(The shape of area when the hints are either W, E, N or S is triangle).
14.2 squares that are different in size, the small one is placed inside the
bigger one, the treasure is somewhere inside the gap between 2
squares. (rare)
15.The treasure is in a region that has mountain
'''
    #MAIN FUNCTIONALITIES
    def __init__(self, count_down: int):
        self.count_down = count_down
        pass
    def hint(self):
        self.count_down -= 1
        pass
    def report(self):
        #report present position
        pass