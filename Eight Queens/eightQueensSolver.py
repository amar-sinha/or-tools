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

def n_queens():
    # Constraint programming engine
    model = cp_model.CpModel()
    n = 8

    

