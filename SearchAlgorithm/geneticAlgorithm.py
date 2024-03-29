from random import randint, choice
import numpy as np
from problem import knapsack, split_data
from math import sqrt, log

plotx = []
ploty = []


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
        begin = int(self.length / 5)
        end = int(self.length * 4/5)
        part = randint(begin, end)
        ta = a[:part]+b[part:]
        tb = b[:part]+a[part:]
        return ta, tb

    def mutation(self, a):
        #mutation with priority tasks
        overW = self.overW(a)
        if overW != 0:
            for i in range(len(a)):
                if randint(0,10)/10 > self.problem.W / overW:
                    a[i] = 0
        else:
            for i in range(len(a)):
                if randint(0,10)/10 < 0.1:
                    a[i] = 1-a[i]
        return a
    
    def overW(self, a):
        w = 0
        for i,j in zip(a, [self.problem[t] for t in range(0,self.length)]):
            if i == 1:
                w += j[2]
        if w > self.problem.W:
            return w
        return 0

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
        
        # score__ = 0
        # if len(_c) > 0:
        #     score__ = -self.problem.getMaxWeight() * len(_c) * 0.5
        # if _w > self.problem.getMaxWeight():
        #     score__ = score__ - _w + self.problem.getMaxWeight()
        #     return _v*0.5 + score__
        
        # return _v *(1-max(0, _w - self.problem.getMaxWeight())-len(_c))

        if _w > self.problem.getMaxWeight():
            return _v/(sqrt(_w-self.problem.getMaxWeight())+len(_c)*len(_c) + 1)
        elif len(_c) > 0:
            return _v/(len(_c) * len(_c) + 1)

        return _v

        

    def selection(self, turns = 6):
        i=0
        maxScore1 = 0
        iindex1 = 0
        maxScore2 = 0
        iindex2 = 0

        while i < turns:
            index = randint(0,self.number_of_gen-1)
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
        next_gen = []
        for _ in range(0, self.number_of_gen, 2):
            p1, p2 = self.selection(log(self.number_of_gen + 1))
            #crossover
            c1, c2 = self.crossover(p1,p2)

            #mutation
            if randint(0,10)/10 < mutation_rate:
                c1,c2 = self.mutation(c1), self.mutation(c2)
            
            next_gen.append(c1)
            next_gen.append(c2)

        self.childs = next_gen

    def fit(self, epochs, view, verbose = 50, mutation_rate=0.1):
        i = 0
        while i < epochs:
            if i % verbose == 0:
                if view == 0:
                    _, b, w, c = self.best_value()
                    print('epoch' ,i, ': v(', b,'), w(',w,'), c(',c,')')
                    # plotx.append(i)
                    # ploty.append(b)
                elif view == 1:
                    scr, chi = self.best_score()
                    print('epoch ' ,i, ': s(', scr,')')
                    # plotx.append(i)
                    # ploty.append(scr)
            self.step(mutation_rate=mutation_rate)
            i += 1

    def __call__(self, problem:knapsack, init = 1000, epochs = 1000, step_report = 100, view = 0, mutation_rate = 0.1) -> None:
        self.extract_neccessary_data(problem=problem)
        self.initialize(init)
        self.fit(epochs=epochs, mutation_rate=mutation_rate, verbose=step_report, view = view)

    def print(self):
        print('___________________________________________')
        for i in self.childs:
            print(self.score(i))
        print('___________________________________________')

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
    data = split_data('input/large_dataset.txt')

    with open('t_OUTPUT_'+str(data.len())+'.txt', 'w') as wf:
        for i in range(data.len()):
            prob = knapsack(data=data[i])
            sol = geneticAl()

            sol(init=10, problem=prob, epochs=5000, mutation_rate=0.1, step_report=100, view = 0)
            result, vmax, _, _ = sol.best_value()

            print(vmax)
            result = str(result)
            wf.write(str(vmax) + '\n')
            wf.write(result + '\n')
            if result != 'None':
                print(result[1:-1])
            else:
                print('None')

            print('----------------------------------------')