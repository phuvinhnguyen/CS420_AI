from problem import knapsack
from bitarray import bitarray as ba
from random import randint

class geneticAl:
    def __init__(self):
        pass

    def initialize(self, init_items:int = 5) -> None:
        self.childs = [self.length*ba('0')]*init_items

    def extract_neccessary_data(self, problem:knapsack):
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

    def crossover(self, a:ba, b:ba):
        part = int(self.length / 2)
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
                if t[0] in tmp_c:
                    tmp_c.remove(t[0])

        ##TODO: ADD INFORMATION TO RESULT AND RETURN IT
        ret_inf = (tmp_v, tmp_w, len(tmp_c)==0)
        
        return ret_inf

    def selection(self, turns = 4):
        i=0
        maxScore = 0
        iindex = 0

        while i < turns:
            index = randint(0,len(self.childs)-1)
            score = self.calculate(self.childs[index])

            tw = 0
            if score[1] > self.maxWeight:
                tw = score[1] - self.maxWeight
            
            score = score[0]*score[0]/(int(score[2])*2 + tw*tw + 1)

            if score > maxScore:
                maxScore = score
                iindex = index
            i += 1

        return (self.childs[iindex], iindex)
    
    def selection_min(self, turns=6):
        i=0
        minScore = -1
        iindex = 0

        while i < turns:
            index = randint(0,len(self.childs)-1)
            score = self.calculate(self.childs[index])

            tw = 0
            if score[1] > self.maxWeight:
                tw = score[1] - self.maxWeight
            
            score = score[0]*score[0]/(int(score[2])*2 + (5*tw)**2 + 1)

            if minScore == -1:
                minScore = score

            if score < minScore:
                minScore = score
                iindex = index
            i += 1

        return iindex

    def step(self, mutation_rate=0.1):
        #crossover
        (a, ia), (b, ib) = self.selection(), self.selection()
        a, b = self.crossover(a,b)

        ria, rib = self.selection_min(), self.selection_min()
        self.childs[ria] = a
        self.childs[rib] = b

        #mutation
        rani = int(randint(0,10) / 10)
        if rani <= mutation_rate:
            t, it = self.selection(1)
            t = self.mutation(t)

            rit = self.selection_min()
            self.childs[rit] = t

    def fit(self, epochs, mutation_rate=0.1):
        i = 0
        while i < epochs:
            self.step(mutation_rate=mutation_rate)
            i += 1

    def __call__(self, problem:knapsack, init = 10, epochs = 100, mutation_rate = 0.1) -> None:
        self.extract_neccessary_data(problem=problem)
        self.initialize(init)
        self.fit(epochs=epochs, mutation_rate=mutation_rate)

    def recent_results(self):
        for i in self.childs:
            print(i, self.calculate(i))

if __name__ == '__main__':
    prob = knapsack('./data.json')
    sol = geneticAl()
    sol(problem=prob, epochs=100)
    print(sol.recent_results())