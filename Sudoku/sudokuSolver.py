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
        soln = []
        for v in self.__variables:
            soln.append(self.Value(v))

        rows = list(self.equal_parts(soln, 9))
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

def Sudoku():
    # Contraint programming engine
    model = cp_model.CpModel()

    print(
        """Enter a Sudoku puzzle as nine (9) rows and nine (9) 
columns of values separated by spaces - enter 0 for 
blank spaces and the given number for preset spaces.
Press Enter after entering the 9th row for solution.""")

    raw_mtrx = []   # raw matrix of each row of puzzle
    id = 1          # unique id for each variable

    # Generate all variables from user input puzzle
    while True:
        row_vals = input().split()
        if row_vals:
            if len(row_vals) != 9:
                print('Incorrect number of columns entered - %s columns' % str(len(row_vals)))
                exit()
            else:
                raw_row = []
                for val in row_vals:
                    if val == '0':
                        raw_row.append(model.NewIntVar(1, 9, str(id)))
                        id +=1
                    else:
                        raw_row.append(model.NewIntVar(int(val), int(val), str(id)))
                        id += 1
                raw_mtrx.append(raw_row)
        else:
            if len(raw_mtrx) != 9:
                print('Incorrect number of rows entered - %s rows' % str(len(raw_mtrx)))
                exit()
            else:
                break

    # Define array of all variables
    main_array = merge(raw_mtrx)

    # Define constraints
    np_mtrx = np.matrix(raw_mtrx)
    for row in np.array(np_mtrx):
        model.AddAllDifferent(row.tolist())
    
    np_mtrx_T = np_mtrx.T
    for col in np.array(np_mtrx_T):
        model.AddAllDifferent(col.tolist())
    
    i, j = 0, 3
    rowset = 0
    colset = 0
    while True:

        if rowset == 0:
            np_mtrx_slice = np_mtrx[0:3, i:j]           
        elif rowset == 1:
            np_mtrx_slice = np_mtrx[3:6, i:j]
        elif rowset == 2:
            np_mtrx_slice = np_mtrx[6:9, i:j]
        else:
            break

        i, j, colset = i+3, j+3, colset+1   
        array = merge(np.asarray(np_mtrx_slice).tolist())
        model.AddAllDifferent(array)
        if colset == 3:
            rowset += 1
            i, j, colset = 0, 3, 0

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

if __name__ == '__main__':
    Sudoku()