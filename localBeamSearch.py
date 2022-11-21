from problem import knapsack, split_data
import numpy as np
from random import randint


weights = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
values = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
class_=[1, 1, 2, 1, 2, 1, 1, 2, 2, 2]
MaxWeight = 101

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
        break

    keep_generate = top(list_of_generate)

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
        if(sol[i] == 1): total_weight += weights[i]
    
    
    if(total_weight <= MaxWeight): return True
    else: return False
    

def value(sol:list):
    #return value of sol
    total_value = 0
    for i in range(0,len(sol)-1):
        if(sol[i] == 1): total_value += values[i]
    return total_value

def top(sol_list:list, t = 5):
    #return top t solutions of the sol list(best solutions)
    list_value = []
    for i in sol_list:
        list_value.append(value(i))
    return []

# def score(sol):
#     #calculate score to use in select top in top function
#     return 0


# print(localBeam(weights,5))
# print(_init_state(weights))
# print(calWeight(_init_state(weights),weights))
print(localBeam([1,1,1,1,1,1,1,1,1,1],weights,5))