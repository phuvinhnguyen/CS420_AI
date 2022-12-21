class agent:
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
    def __init__(self, init_place:list(int, int), map_size:list(int, int)):
        self.pos = init_place[:]
        self.mask = [['']*map_size[0] for _ in range(map_size[1])]
        pass
    def step(self, info):
        pass
    def report(self):
        pass