from problem import knapsack, split_data


def bruteForce(maxWeight,C,weight,value,c):
    #initial state 0x00...00
    i=0
    #max score
    maxS = 0
    #result
    result = ''
    #iterate though all solutions
    while i != (1 << len(value)):
        num = bin(i)[2:]
        solution = '0'*(len(value) - len(num)) + num
        _v,_w,_c = 0,0,[j for j in range(1,C+1)]

        for it in range(len(solution)):
            if '1' == solution[it]:
                _v += int(value[int(it)])
                _w += int(weight[int(it)])
                if int(c[int(it)]) in _c:
                    _c.remove(int(c[int(it)]))
        
        if _w > maxWeight or len(_c) > 0:
            _v = 0
        
        if _v > maxS:
            maxS = _v
            result = solution
        
        i += 1

    return maxS, str([int(i) for i in result])[1:-1]

if __name__ == '__main__':
    data = split_data('input/small_dataset.txt')

    with open('output/OUTPUT_'+str(data.len())+'.txt', 'w') as wf:
        for i in range(data.len()):
            prob = knapsack(data=data[i])
            maxV, sol = bruteForce(prob.getMaxWeight(), prob.getClassNum(), prob.w, prob.v, prob.c,)
            print(maxV)
            print(sol)