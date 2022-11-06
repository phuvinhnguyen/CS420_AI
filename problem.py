import json

class knapsack:
    '''
    data file structure example:
    {
        "max weight": 5,
        "class"     : ['red','green','red'],
        "value"     : [2,3,1],
        "weight"    : [3,2,1],
        "quatity"   : [3,2,1]
    }

    data in this class:
    - self.c: class         (str list)
    - self.W: max weight    (float)
    - self.w: weight        (float list)
    - self.v: value         (float list)
    - self.q: quatity       (int list)
    '''
    def __init__(self, path='./data.json'):
        with open(path) as rf:
            data = json.load(rf)
            self.c = data['class']
            self.W = data['max weight']
            self.v = data['value']
            self.w = data['weight']
            self.q = data['quatity']
        
    
