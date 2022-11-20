from problem import knapsack, split_data
import numpy as np


def getKBestValues(k,arr):
    tmp_arr = arr.copy()
    tmp_arr.sort()
    tmp_arr.reverse()
    res = []
    index = []
    for i in range(0,k):
        res.append(tmp_arr[i])
        index.append(arr.index(tmp_arr[i]))
    return (res,index)

#heuristic: k highest values
def localBeam(weights,class_,values,k):
    state = []
    states_list = []
    for i in range(0,len(weights)):
        state.append()
    return 0

def checkWeight(index,weights):
    total = 0
    for i in range(0,len(index)):
        total += weights[i]
        print(index[i])
    return total
    

weights = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
values = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
class_=[1, 1, 2, 1, 2, 1, 1, 2, 2, 2]

states = [([95, 85, 55, 52, 48],[5,0,8,9,2])]
# test(weights,5)

# re = getKBestValues(5,weights)
# print(re)
print(checkWeight([5,0,8,9,2],[95, 85, 55, 52, 48]))
