from problem import knapsack, split_data
import numpy as np
from random import randint
import sys
sys.setrecursionlimit(1500)


k = 1
# initial state will be [1,1,1,1,1,..,1] -> each item will have 1 so the total weight will be over the max weight can have
# we reduce the number of item one by one (these are successors of initial state) randomly with heuristic : remove the lowest value first
# after removed item until the weight is lower than max weight, we will check if we can add any small-weight item
    

def localBeam(init, weights,k):
    if valid(init):
        return value(init), init
    if 1 not in init or fullClass(init) == False:
        return 0, [0]*len(weights)

    #list of acceptable state
    list_of_generate = []
    #reduce item in the init state in the descending order of value (heuristic)
    for i in range(len(init)):
        if init[i] == 1:
            x = init.copy()
            x[i] = 0
            list_of_generate.append(x)
    keep_generate = top(list_of_generate, k)
    bestV = 0
    result = None
    
    for a in keep_generate:
        v, sol = localBeam(a, weights, k)
        if v >= bestV:
            bestV = v
            result = sol
    
    return bestV, result

def valid(sol:list):
    #return true if sol is valid
    total_weight = 0
    c = classnum
    for i in range(0,len(sol)-1):
        if(sol[i] == 1):
            total_weight += int(weights[i])
            if classes[i] in c:
                c.remove(classes[i])
    
    if(total_weight <= MaxWeight and len(c) == 0): return True
    else: return False

def overWeight(sol: list):
    total_weight = 0
    for i in range(0,len(sol)-1):
        if(sol[i] == 1):
            total_weight += weights[i]
            if total_weight > MaxWeight:
                return True
    return False

def fullClass(sol: list):
    c = classnum
    for i in range(0,len(sol)-1):
        if(sol[i] == 1):
            if int(classes[i]) in c:
                c.remove(int(classes[i]))
    
    if len(c) == 0:
        return True
    return False

def value(sol:list):
    #return value of sol
    total_value = 0
    for i in range(0,len(sol)-1):
        if(sol[i] == 1):
            total_value += int(values[i])
    return total_value

def top(sol_list:list, t = 5):
    #return top t solutions of the sol list(best solutions)
    list_value = []
    for i in sol_list:
        list_value.append(score(i))
    tmp = list_value.copy()

    indexs = sorted(range(len(tmp)), key=lambda i: tmp[i])[-t:]

    tmp.sort()
    tmp.reverse()
    index = []
    for i in indexs:
         index.append(sol_list[i])

    return index

def score(sol):
    #calculate score to use in select top in top function
    if fullClass(sol) == False:
        return 0
    return value(sol)


# print(localBeam(weights,5))
# print(_init_state(weights))
# print(calWeight(_init_state(weights),weights))
# print(localBeam([1,1,1,1,1,1,1,1,1,1],weights,5))

if __name__ == '__main__':
    data = split_data('input/large_dataset.txt')

    with open('output/OUTPUT_'+str(data.len())+'.txt', 'w') as wf:
        for i in range(data.len()):
            prob = knapsack(data=data[i])
            values = prob.v
            weights = prob.w
            classes = prob.c
            MaxWeight = prob.getMaxWeight()
            classnum = [k for k in range(1,1+prob.getClassNum())]
            init = []
            for i in range(0,len(weights)-1):
                init.append(1)
            bestV, sol = localBeam(init,weights,k)
            print(bestV)
            print(str(sol)[1:-1])
   