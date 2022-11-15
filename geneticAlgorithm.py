import problem
from bitarray import bitarray as ba
from random import randint

class geneticAl:
    def __init__(self):
        pass

    def initialize(self, init_items:int = 5) -> None:
        self.childs = [self.length*ba('0')]*init_items

    def extract_neccessary_data(self, problem:problem.knapsack):
        '''
        return length_of_each_item, list_of_begin_index
        '''
        self.length = 0
        self.maxWeight = problem.getMaxWeight()
        self.denote = []
        self.item_class = []
        for i in range(problem.len()):
            tmp = problem[i]
            self.length += tmp[-1]
            self.denote.append(tmp[0:-1])
            if tmp[0] not in self.item_class:
                self.item_class.append(tmp[0]) 

    def crossover(self, a:ba, b:ba, part:int):
        ta = a[:part]+b[part:]
        tb = b[:part]+a[part:]
        return ta, tb

    def mutation(self, a:ba):
        pos = randint(0, self.length-1)
        a[pos] = 1-a[pos]
        return a

    def calculate(self, child:ba):
        tmp_v = 0
        tmp_w = 0
        tmp_c = self.item_class
        for (b,t) in zip(child, self.denote):
            if b == 1:
                tmp_v += t[1]
                tmp_w += t[2]
                tmp_c.remove(t[0])

        ##TODO: ADD INFORMATION TO RESULT AND RETURN IT
        ret_inf = (tmp_v, tmp_w, len(tmp_c)==0)
        
        return ret_inf

    def selection(self, turns = 3):
        i=0
        maxScore = 0
        iindex = 0

        while i < turns:
            index = randint(0,len(self.childs))
            score = self.calculate(self.childs[index])

            tw = 0
            if score[1] > self.maxWeight:
                tw = score[1] - self.maxWeight
            
            score = score[0]*score[0]/(score[2]*2 + tw*tw)

            if score > maxScore:
                maxScore = score
                iindex = index
            i += 1

        return self.childs[iindex]
    
    def fit_gen(self, mutation_rate):
        
        pass

    def fit(self, epochs, mutation_rate):
        pass

    def __call__(self, problem:problem.knapsack) -> problem.result:
        pass


if __name__ == '__main__':
    a = ba('0100100')
    b = ba('1100011')
    a[0]=1-a[0]
    print(a)