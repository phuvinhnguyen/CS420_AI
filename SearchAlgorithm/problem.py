class split_data:
    '''
    this class get a file name, read that file and save the set of dataset in that file
    (1 file may contain many datasets)
    '''
    def __init__(self, path='./INPUT_x.txt'):
        with open(path) as rf:
            self.data = rf.readlines()
    
    def __getitem__(self, key:int):
        '''
        return dataset at index key
        '''
        return self.data[key*5:key*5+5]
    
    def len(self):
        '''
        return number of dataset in a file
        '''
        return int(len(self.data) / 5)


class knapsack(object):
    def __init__(self, data):
        self.W = int(data[0])
        self.c_num = int(data[1])

        self.w = data[2].split(',')
        self.v = data[3].split(',')
        self.c = data[4].split(',')

    def __getitem__(self, key:int):
        '''
        return item at index key
        item index n will be (class[n], value[n], weight[n])
        or (class_of_item, value_of_item, weight_of_item)
        '''
        return (int(self.c[key]), int(self.v[key]), int(self.w[key]))

    def getMaxWeight(self):
        '''
        return W of dataset
        '''
        return self.W

    def getClassNum(self):
        '''
        return number of class in the dataset
        '''
        return self.c_num

    def len(self):
        '''return number of items'''
        return len(self.c)