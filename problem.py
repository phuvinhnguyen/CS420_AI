class knapsack(object):
    def __init__(self, path='./INPUT_x.txt'):
        with open(path, 'r') as rf:
            data = rf.readlines()

            self.W = int(data[0])
            self.c_num = int(data[1])

            self.w = data[2].split(',')
            self.v = data[3].split(',')
            self.c = data[4].split(',')

    def __getitem__(self, key:int):
        '''item index n will be (class[n], value[n], weight[n])'''
        return (int(self.c[key]), int(self.v[key]), int(self.w[key]))

    def getMaxWeight(self):
        return self.W

    def getClassNum(self):
        return self.c_num

    def len(self):
        '''return number of items'''
        return len(self.c)