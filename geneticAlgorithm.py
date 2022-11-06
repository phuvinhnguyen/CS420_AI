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
        pass

    def __call__(self, problem:problem.knapsack) -> problem.result:
        pass


if __name__ == '__main__':
    a = ba(
        '110'
    )

    print(a)
    pass