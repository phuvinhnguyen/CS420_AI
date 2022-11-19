from random import randint
import numpy as np

def generate(filename:str, test_number: int = 10, mode:int = 0):
    '''
    mode: 0->small dataset, 1->large dataset
    '''
    with open('./input/'+filename, 'w') as wf:
        for i in range(test_number):
            wf.write(str(randint(0,2000))+'\n')
            if mode == 0:
                C = randint(2,5)
                wf.write(str(C)+'\n')
                size = randint(10,40)
                w,v,c = [],[],[]
                for _ in range(size):
                    w.append(randint(0,2500))
                    v.append(randint(0,3000))
                    c.append(randint(1,C))

                wf.write(str(w)[1:-1]+'\n')
                wf.write(str(v)[1:-1]+'\n')
                wf.write(str(c)[1:-1]+'\n')
            elif mode == 1:
                C = randint(6,10)
                wf.write(str(C)+'\n')
                size = randint(50,1000)
                w,v,c = [],[],[]
                for _ in range(size):
                    w.append(randint(0,2500))
                    v.append(randint(0,3000))
                    c.append(randint(1,C))

                wf.write(str(w)[1,-1]+'\n')
                wf.write(str(v)[1,-1]+'\n')
                wf.write(str(c)[1,-1]+'\n')


if __name__=='__main__':
    generate('test.txt')