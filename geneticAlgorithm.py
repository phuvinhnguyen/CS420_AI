import problem
from bitarray import bitarray as ba

class geneticAl:
    def __init__(self):
        pass

    def initialize(self, length:int, init_items:int = 5) -> None:
        pass

    def extract_neccessary_data(self, problem:problem.knapsack):
        '''
        return length_of_each_item, list_of_begin_index
        '''
        self.size = 0
        self.maxWeight = problem.getMaxWeight()
        self.denote = []
        self.item_class = []
        for i in range(problem.len()):
            tmp = problem[i]
            self.size += tmp[-1]
            self.denote.append(tmp[0:-1])
            if tmp[0] not in self.item_class:
                self.item_class.append(tmp[0]) 

    def calculate(self, childs:list[ba]):
        result = []
        for child in childs:
            tmp_v = 0
            tmp_w = 0
            tmp_c = self.item_class
            for (b,t) in zip(child, self.denote):
                if b == 1:
                    tmp_v += t[1]
                    tmp_w += t[2]
                    tmp_c.remove(t[0])

            ##TODO: ADD INFORMATION TO RESULT AND RETURN IT

    def __call__(self, problem:problem.knapsack) -> problem.result:
        pass


if __name__ == '__main__':
    a = [1,2,3,6,5]

    print(a.remove(2))
    print(a)
    pass