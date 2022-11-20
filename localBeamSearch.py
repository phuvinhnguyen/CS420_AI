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
def _init_state(weights):
    first_state = [1]*len(weights)
    return first_state

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

    keep_generate = top(list_of_generate)

    bestV = 0
    result = None
    for i in keep_generate:
        v, sol = localBeam(i, weights, k)
        if v >= bestV:
            bestV = v
            result = sol
    
    return bestV, result

def top(sol_list):
    return []

def score(sol):
    return 0

# get value to compare the best value later
def calValue(state,values):
    total = 0
    for i in range(0,len(state)):
        if(state[i] == 1): total += values[i]
    return total

# get weight to check current weight is lower than max weight
def calWeight(state,weights):
    cur_weight = 0
    for i in range(0,len(state)):
        if(state[i] == 1): cur_weight += weights[i]
    return cur_weight

#check if can add more value if the current state weight is lower than max weight
def checkAdd(state):
    for s in state:
        if s == 0:
            s = 1
            if (calWeight(state,weights) < MaxWeight): break
            else: s = 0

print(localBeam(weights,5))