from __future__ import print_function
from ortools.sat.python import cp_model
import numpy as np

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    ## Print intermediate solutions

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def equal_parts(self, l, n): 
        for i in range(0, len(l), n):  
            yield l[i:i + n] 

    def on_solution_callback(self):
        self.__solution_count += 1
        soln = []
        for v in self.__variables:
            soln.append(self.Value(v))

        row_len = int(np.sqrt([len(soln)]))
        rows = list(self.equal_parts(soln, row_len))
        for row in rows:
            print(row)

    def solution_count(self):
        return self.__solution_count

def merge(mtrx_list):
    # use this function to merge a list of lists into one single list
    merged = []
    for row in mtrx_list:
        merged += row
    
    return merged

def addMagicSquaresRowVal(model, row, magic, val, id):
    if val == '0':
        row.append(model.NewIntVar(1, magic, str(id)))
        id += 1
    else:
        row.append(model.NewIntVar(int(val), int(val), str(id)))
        id += 1

def makeMagicSquaresRow(model, normality, row, magic, val, id):
    if 0 <= int(val) <= magic:
        addMagicSquaresRowVal(model, row, magic, val, id)
    else:
        print('A value entered in this row exceeds the range of values [1,%i] for the normal magic square' % magic)
        exit()

def magicSquares():
    # Constraint programming engine
    model = cp_model.CpModel()

    print(
        """Enter a magic square of n by n size as n rows and n 
columns of values separated by spaces - enter 0 for 
blank spaces and the given number for preset spaces.
Press Enter after entering the nth row for solution."""
    )

    raw_mtrx = []   # raw matrix of each row of magic square
    id = 1          #  unique id for each variable
    n = int(input("Size of puzzle: "))
    normality = input("Is the magic square normal? (y/n): ")
    magic_sum = -1
    if normality == 'n':
        magic_sum = int(input("Enter the magic sum: "))

    # Generate all variables from user input magic square
    while True:
        row_vals = input().split()
        if row_vals:
            if normality == 'y':
                magic_sum = int(n*(n*n+1)/2) # Normal Magic Sum is defined as M = n(n^2+1)/2
                magic = n*n
            else:
                magic = magic_sum
            if len(row_vals) != n:
                print('Incorrect number of columns entered - %s columns' % str(len(row_vals)))
                exit()
            else:
                raw_row = []
                for val in row_vals:
                    makeMagicSquaresRow(model, normality, raw_row, magic, val, id)
                raw_mtrx.append(raw_row)
        else:
            if len(raw_mtrx) != n:
                print('Incorrect number of rows entered - %s rows' % str(len(raw_mtrx)))
                exit()
            else:
                break

    # Define constraints (all rows, columns, and diagonals must sum to equal the magic sum)
    np_mtrx = np.matrix(raw_mtrx)
    for row in np.array(np_mtrx):
        model.Add(sum(row) == magic_sum)
    
    np_mtrx_T = np_mtrx.T
    for col in np.array(np_mtrx_T):
        model.Add(sum(col) == magic_sum)

    diagonals = [np_mtrx.diagonal(), np.fliplr(np_mtrx).diagonal()]
    for diag in diagonals:
        model.Add(sum(np.asarray(diag).tolist()[0]) == magic_sum)

    # Define array of all variables
    main_array = merge(raw_mtrx)

    # Solve model
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(main_array)
    status = solver.SearchForAllSolutions(model, solution_printer)

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())
    print('  - solutions found : %i' % solution_printer.solution_count())

if __name__ == "__main__":
    magicSquares()