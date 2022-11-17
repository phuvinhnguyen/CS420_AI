from random import randint
import numpy as np
from problem import knapsack, split_data
from math import sqrt

class geneticAl:
    def __init__(self):
        pass

    def initialize(self, init_items:int = 5) -> None:
        self.childs = []
        for i in range(init_items):
            self.childs.append(list(np.random.randint(0, 2, self.length)))

    def extract_neccessary_data(self, problem:knapsack):
        self.length = problem.len()
        self.item_class = [i for i in range(1,problem.c_num+1)]
        self.problem = problem

    def crossover(self, a, b):
        part = randint(0,self.length-1)
        ta = a[:part]+b[part:]
        tb = b[:part]+a[part:]
        return ta, tb

    def mutation(self, a):
        for i in range(len(a)):
            if randint(0,10)/10 < 0.35:
                a[i] = 1-a[i]
        return a
    
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
            return _v/(abs(_w-self.problem.getMaxWeight()) + 1)
        elif len(_c) > 0:
            return _v*0.7

        return _v

    def selection(self, turns = 6):
        i=0
        maxScore = 0
        iindex = 0

        while i < turns:
            index = randint(0,len(self.childs)-1)
            score = self.score(self.childs[index])

            if score > maxScore:
                maxScore = score
                iindex = index
            i += 1

        return self.childs[iindex]

    def step(self, mutation_rate=0.1):
        #select
        selected = [self.selection(int(sqrt(self.length))) for _ in range(self.problem.len())]

        next_gen = list()
        for i in range(0, self.problem.len()-1, 2):
            p1, p2 = selected[i], selected[i+1]
            c1,c2 = self.crossover(p1,p2)

            if randint(0,10)/10 > mutation_rate:
                c1,c2 = self.mutation(c1), self.mutation(c2)
            
            next_gen.append(c1)
            next_gen.append(c2)
        
        self.childs = next_gen

    def fit(self, epochs, verbose = 50, mutation_rate=0.1):
        i = 0
        while i < epochs:
            self.step(mutation_rate=mutation_rate)
            if i % verbose == 0:
                _, b, w, c = self.best_value()
                print('epoch ' ,i, ': v(', b,'), w(',w,'), c(',c,')')
            i += 1

    def __call__(self, problem:knapsack, init = 1000, epochs = 1000, verbose = 100, mutation_rate = 0.1) -> None:
        self.extract_neccessary_data(problem=problem)
        self.initialize(init)
        self.fit(epochs=epochs, mutation_rate=mutation_rate, verbose=verbose)

    def print(self):
        for i in self.childs:
            print(i, self.score(i))

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
    data = split_data('small_dataset.txt')

    for i in range(data.len()):
        prob = knapsack(data=data[1])
        sol = geneticAl()

        sol(init=100, problem=prob, epochs=100, mutation_rate=0.3, verbose=25)
        result, vmax, _, _ = sol.best_value()

        print(vmax)
        result = str(result)
        if result != 'None':
            print(result[1:-1])
        else:
            print('None')

        print('----------------------------------------')