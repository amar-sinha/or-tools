from __future__ import print_function
from ortools.sat.python import cp_model
import numpy as np

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    # Print intermediate solutions

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def equal_parts(self, l, n): 
        for i in range(0, len(l), n):  
            yield l[i:i + n] 

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count

def n_queens(n):
    # Constraint programming engine
    model = cp_model.CpModel()

    #queen_mtrx = [model.NewIntVar(0, n-1, 'col%i' % i) for i in range(n)]

    raw_mtrx = []
    count = 0
    id = 1
    while count < n:
        raw_row = []
        for i in range(n):
            raw_row.append(model.NewIntVar(0,1, str(id)))
            id += 1
        raw_mtrx.append(raw_row)
        count += 1

    queen_mtrx = np.matrix(raw_mtrx)

    print(queen_mtrx)

    return queen_mtrx

if __name__ == '__main__':
    n_queens(4)