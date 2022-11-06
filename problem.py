import json

class knapsack(object):
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

    NOTE: len(class) = len(value) = len(weight) = len(quatity)
        - item index n will be (class[n], value[n], weight[n], quatity[n])
    '''
    def __init__(self, path='./data.json'):
        with open(path) as rf:
            data = json.load(rf)
            self.c = data['class']
            self.W = data['max weight']
            self.v = data['value']
            self.w = data['weight']
            self.q = data['quatity']

    def __getitem__(self, key):
        '''item index n will be (class[n], value[n], weight[n], quatity[n])'''
        return (self.c[key], self.v[key], self.w[key], self.q[key])

    def len(self):
        '''return number of items'''
        return len(self.c)
        
    
class result:
    '''
    the quatity of each item that we take:
    for ex:
        self.res = [1,2,1] means: take 1 from item 1, 2 from item 2, 1 from item 3
    '''
    def __init__(self, res:list):
        self.res = res