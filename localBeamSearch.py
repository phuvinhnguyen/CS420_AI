from problem import knapsack, split_data
import numpy as np
from random import randint



k = 3
# initial state will be [1,1,1,1,1,..,1] -> each item will have 1 so the total weight will be over the max weight can have
# we reduce the number of item one by one (these are successors of initial state) randomly with heuristic : remove the lowest value first
# after removed item until the weight is lower than max weight, we will check if we can add any small-weight item
    

def localBeam(init, weights,k):
    if 1 not in init:
        return 0, None

    #list of acceptable state
    list_of_generate = []
    #reduce item in the init state in the descending order of value (heuristic)
    for i in range(len(init)):
        if i == 0:
            continue
        x = init
        x[i] = 0
        list_of_generate.append(x)

    keep_generate = top(list_of_generate,k)


    bestV = 0
    result = None
    if valid(init) == True:
        bestV = value(init)
        result = init
    for i in keep_generate:
        v, sol = localBeam(i, weights, k)
        if v >= bestV:
            bestV = v
            result = sol
    
    return bestV, result

def valid(sol:list):
    #return true if sol is valid
    total_weight = 0
    for i in range(0,len(sol)-1):
        if(sol[i] == 1): total_weight += int(weights[i])
    
    
    if(total_weight <= MaxWeight): return True
    else: return False
    

def value(sol:list):
    #return value of sol
    total_value = 0
    for i in range(0,len(sol)-1):
        if(sol[i] == 1): total_value += int(values[i])
    return total_value

def top(sol_list:list, t = 5):
    #return top t solutions of the sol list(best solutions)
    list_value = []
    for i in sol_list:
        list_value.append(value(i))
    tmp = list_value.copy()
    tmp.sort()
    tmp.reverse()
    index = []
    for i in range(0,t-1):
         index.append(list_value.index(tmp[i]))
    res = []
    for i in range(0,t-1):
        res.append(sol_list[index[i]])
    return res

# def score(sol):
#     #calculate score to use in select top in top function
#     return 0


# print(localBeam(weights,5))
# print(_init_state(weights))
# print(calWeight(_init_state(weights),weights))
# print(localBeam([1,1,1,1,1,1,1,1,1,1],weights,5))

if __name__ == '__main__':
    data = split_data('input/small_dataset.txt')

    with open('output/OUTPUT_'+str(data.len())+'.txt', 'w') as wf:
        for i in range(data.len()):
            prob = knapsack(data=data[i])
            values = prob.v
            weights = prob.w
            MaxWeight = int(prob.getMaxWeight())
            init = []
            for i in range(0,len(weights)-1):
                init.append(1)
            print(init)
            print(type(init))
            bestV, sol = localBeam(init,weights,k)
            print(bestV)
            print(sol)
   