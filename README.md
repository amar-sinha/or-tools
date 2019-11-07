# Google OR-Tools
## Constraint Programming

_<h4>Project implementations utilizing the Google OR-Tools packages for constraint programming.</h4>_

### <u>Goal</u>
This repository contains projects that make use of the Google OR-Tools constraint programming package. It is intended to showcase implementations of constraint programming to solve various combinatorial problems.

### <u>Package Installation</u>
Install ortools

    $ python -m pip install --upgrade --user ortools

Install numpy

    $ pip install numpy

### <u>OR-Tools Specifications</u>
Constraints define the unique and specific properties of a solution we want to be found. Listed below are constraints that are used throught these project implementations: 

- `AddAllDifferent` - forces all variables provided as input to have different values 

Statuses are descriptions of the results of the model being tested. There are five possible statuses:
- `INFEASIBLE` - returned when it is proven that no solutions are to be found. 
- `FEASIBLE` - returned when some solutions are found. 
- `OPTIMAL` - returned when all solutions have been found. 
- `MODEL_INVALID` - returned when the model does not pass the validation step.
- `UNKNOWN` - returned when a search limit is reached and no solution has been found.

### <u>Project Descriptions</u>
* <a href='https://github.com/amar-sinha/or-tools/tree/master/Sudoku%20Solver'>_Sudoku Solver_</a> - The Sudoku Solver takes a 9x9 Sudoku puzzle as user input. The user enters nine rows and nine columns of values separated by spaces, where blank spaces are entered as 0 and preset spaces are entered as the given number. 
    * _Create a matrix of all variables_ - The program first creates uniquely identified NewIntVar integer variables and organizes them in a 9x9 NumPy matrix.
    * _Define and add constraints_ - The `AddAllDifferent` constraint is applied to the Sudoku puzzle to fill unique values of 1-9 in each row, column, and 3x3 subsquare. To add each constraint:
        * _Rows_ -  iterate through each row of the matrix stored as a NumPy array to add each row constraint
        * _Columns_ - iterate through each row of the transpose of the matrix (i.e. the columns of the original matrix) stored as a NumPy array to add each column constraint
        * _Subsquares_ - iteratively create 3x3 slices for each subsquare in each three-row set and three-column set and add each subsquare constraint
    * _Generate and call the solution_ - Generate the solution using `cp_model.CpSolver()` and call back the solution found for each block of the Sudoku puzzle. From a list of all 81 variables, split the list into equal sections of 9 values using the `equal_parts` method created, and output each row to generate the completed Sudoku Puzzle.
    * _Provide runtime statistics_ - The program provides the user with insight to the program by outputting the status, the number of conflicts, the number of search branches, the time the program took to complete, and the total number of solutions found.