import json

class knapsack(object):
    def __init__(self, path='./INPUT_x.txt'):
        with open(path, 'r') as rf:
            data = rf.readlines()

            self.W = int(data[0])
            self.c_num = int(data[1])

            self.w = data[2].split(',')
            self.v = data[3].split(',')
            self.c = data[4].split(',')
            # self.W = data['max weight']
            # self.v = data['value']
            # self.w = data['weight']
            # self.q = data['quatity']

    def __getitem__(self, key:int):
        '''item index n will be (class[n], value[n], weight[n], quatity[n])'''
        return (self.c[key], self.v[key], self.w[key])

    def getMaxWeight(self):
        return self.W

    def getClassNum(self):
        return self.c_num

    def len(self):
        '''return number of items'''
        return len(len(self.c))
        
    
# class result:
#     '''
#     the quatity of each item that we take:
#     for ex:
#         self.res = [1,2,1] means: take 1 from item 1, 2 from item 2, 1 from item 3
#     '''
#     def __init__(self, res:list):
#         self.res = res