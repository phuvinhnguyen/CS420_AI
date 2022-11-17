from random import randint
import numpy as np
from problem import knapsack, split_data
from math import sqrt, log

class geneticAl:
    def __init__(self):
        pass

    def initialize(self, init_items:int = 5) -> None:
        self.childs = []
        self.number_of_gen = init_items
        for i in range(init_items):
            self.childs.append(list(np.random.randint(0, 2, self.length)))

    def extract_neccessary_data(self, problem:knapsack):
        self.length = problem.len()
        self.item_class = [i for i in range(1,problem.c_num+1)]
        self.problem = problem

    def crossover(self, a, b):
        part = randint(1,self.length-1)
        ta = a[:part]+b[part:]
        tb = b[:part]+a[part:]
        return ta, tb

    def mutation(self, a):
        #mutation with priority tasks
        if self.overW(a):
            for i in range(len(a)):
                if randint(0,10)/10 < 0.35:
                    a[i] = 0
        else:
            for i in range(len(a)):
                if randint(0,10)/10 < 0.35:
                    a[i] = 1-a[i]
        return a
    
    def overW(self, a):
        w = 0
        for i,j in zip(a, [self.problem[t] for t in range(0,self.length)]):
            if i == 1:
                w += j[2]
            if w > self.problem.W:
                return True
        return False

    def score(self, a):
        _w = 0
        _v = 0
        _c = self.item_class
        for (i,j) in zip(a,[self.problem[t] for t in range(0,self.length)]):
            if i == 1:
                _w += j[2]
                _v += j[1]
                if j[0] in _c:
                    _c.remove(j[0])
        
        if _w > self.problem.getMaxWeight():
            return log(_v)/(abs(_w-self.problem.getMaxWeight()))
        elif len(_c) > 0:
            return _v*0.1

        return _v + 10

    def selection(self, turns = 6):
        i=0
        maxScore1 = 0
        iindex1 = 0
        maxScore2 = 0
        iindex2 = 0

        while i < turns:
            index = randint(0,len(self.childs)-1)
            score = self.score(self.childs[index])

            if score > maxScore1:
                maxScore1 = score
                iindex1 = index
            elif score > maxScore2 and index != iindex1:
                maxScore2 = score
                iindex2 = index
            i += 1

        return self.childs[iindex1], self.childs[iindex2]

    def removei(self, turns = 6):
        i=0
        minScore1 = self.score(self.childs[0])
        iindex1 = 0
        minScore2 = self.score(self.childs[0])
        iindex2 = 0

        while i < turns:
            index = randint(0,len(self.childs)-1)
            score = self.score(self.childs[index])

            if score < minScore1:
                minScore1 = score
                iindex1 = index
            elif score < minScore2 and index != iindex1:
                minScore2 = score
                iindex2 = index
            i += 1

        return iindex1, iindex2

    def step(self, mutation_rate=0.1):
        #select
        #selected = [self.selection(int(log(self.length)) + 3) for _ in range(self.problem.len())]

        for i in range(0, self.number_of_gen):
            #choose parent
            p1, p2 = self.selection(sqrt(self.number_of_gen))
            #crossover
            c1,c2 = self.crossover(p1,p2)

            #mutation
            if randint(0,10)/10 < mutation_rate:
                c1,c2 = self.mutation(c1), self.mutation(c2)
            
            iindex1, iindex2 = self.removei(sqrt(self.number_of_gen))
            self.childs[iindex1], self.childs[iindex2] = c1,c2

    def fit(self, epochs, view, verbose = 50, mutation_rate=0.1):
        i = 0
        while i < epochs:
            self.step(mutation_rate=mutation_rate)
            if i % verbose == 0:
                if view == 0:
                    _, b, w, c = self.best_value()
                    print('epoch ' ,i, ': v(', b,'), w(',w,'), c(',c,')')
                elif view == 1:
                    scr, chi = self.best_score()
                    print('epoch ' ,i, ': s(', scr,')')
            i += 1

    def __call__(self, problem:knapsack, init = 1000, epochs = 1000, verbose = 100, view = 0, mutation_rate = 0.1) -> None:
        self.extract_neccessary_data(problem=problem)
        self.initialize(init)
        self.fit(epochs=epochs, mutation_rate=mutation_rate, verbose=verbose, view = view)

    def print(self):
        for i in self.childs:
            print(i, self.score(i))

    def best_score(self):
        max = 0
        chi = None
        for child in self.childs:
            s = self.score(child)
            if s > max:
                max = s
                chi = child
        
        return max, chi

    def best_value(self):
        vmax = 0
        w = 0
        c = 0
        result = None
        for child in self.childs:
            _v, _w, _c = 0, 0, self.item_class
            for (i, j) in zip(child, [self.problem[t] for t in range(0, self.length)]):
                if i == 1:
                    _v += j[1]
                    _w += j[2]
                    if j[0] in _c:
                        _c.remove(j[0])
            if _w < self.problem.getMaxWeight() and len(_c) == 0 and _v > vmax:
                vmax = _v
                result = child
                w = _w
                c = len(_c)
        
        return result, vmax, w, c
                
if __name__ == '__main__':
    data = split_data('large_dataset.txt')


    for i in range(data.len()):
        prob = knapsack(data=data[i])
        sol = geneticAl()

        sol(init=100, problem=prob, epochs=10, mutation_rate=0.3, verbose=5, view = 0)
        result, vmax, _, _ = sol.best_value()

        print(vmax)
        result = str(result)
        if result != 'None':
            print(result[1:-1])
        else:
            print('None')

        print('----------------------------------------')