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

- `Add` - adds a BoundedLinearExpression to the model
- `AddAllDifferent` - forces all variables provided as input to have different values 

Statuses are descriptions of the results of the model being tested. There are five possible statuses:
- `INFEASIBLE` - returned when it is proven that no solutions are to be found. 
- `FEASIBLE` - returned when some solutions are found. 
- `OPTIMAL` - returned when all solutions have been found. 
- `MODEL_INVALID` - returned when the model does not pass the validation step.
- `UNKNOWN` - returned when a search limit is reached and no solution has been found.

### <u>Project Descriptions</u>
* <a href='https://github.com/amar-sinha/or-tools/tree/master/Cryptarithmetic'>_Cryptarithmetic_</a> - The Cryptarithmetic Puzzle Solver takes some _n_ number of words in from user input. For the _n_ words, all words up to the (_n_-1)th word will sum up to equal the (_n_)th word.
    * _Create word and letter arrays_ - The program first reads each string for the left-hand side and right-hand sides of the equations. It generates a `word_array` (contains whole words) and a `split_word_array` (a list of lists where each list contains split words).
    * _Creating the variables_ - To obtain a NewIntVar integer variable for each unique letter in the equation, the program iterates through each character in each word of the split word array and adds the { character : NewIntVar } key-value pair to the `letters_dict`.
    * _Define and add constraints_ - The `AddAllDifferent` constraint is applied to `intvar_array`, which is the values set of `letters_dict`, to ensure that each unique letter has a unique value. The `Add` constraint is applied to the equation generated in the for loop that iterates through the split word array. The inner for loop creates a numerical value for each particular word by generating a digit for each place value, which is then added to the constraint array.
    * _Generate and call the solution_ - Generate the solution using `cp_model.CpSolver()` and call back the solution found for each unique letter - showing all possible solutions for the puzzle.
    * _Provide runtime statistics_ - The program provides the user with insight to the program by outputting the status, the number of conflicts, the number of search branches, the time the program took to complete, and the total number of solutions found.

* <a href='https://github.com/amar-sinha/or-tools/tree/master/Magic%20Squares'>_Magic Squares_</a> - The Magic Squares Solver takes a magic square, the normality of the puzzle, and the magic sum for a non-normal puzzle as user input. The user enters n rows and n colums of values separated by spaces, where blank spaces are entered as 0 and preset spaces are entered as the given number.
    * _Get normality and size of puzzle_ - Ask the user if the puzzle for the size of the puzzle and if it is normal or not - this affects what the magic sum of the puzzle will be. A normal puzzle contains values restricted to the range [1, n<sup>2</sup>] and is solved with the magic sum calculated using the formula: M<sub>n</sub> = [n(n<sup>2</sup>+1)] / 2. A non-normal puzzle is contains values restricted to no range and is solved with a magic sum specified by the user.
    * _Create a matrix of all variables_ - The program creates a matrix of size _n_ composed of uniquely identified NewIntVar integer variables.
    * _Define and add constraints_ - The `Add` constraint is applied to the Magic Square to ensure that the summation of each row, column, and diagonal equals the magic sum.
        * _Rows_ - iterate through each row of the matrix stored as a NumPy array to add each row contraint
        * _Columns_ - iterate through each row of the transpose of the matrix (i.e. the columns of the original matrix) stored as a NumPy array to add each column constraint
        * _Diagonals_ - add the constraint to each diagonal using the `diagonal()` method on the original matrix and the reflection of the matrix obtained using the `np.fliplr` function
    * _Generate and call the solution_ - Generate the solution using `cp_model.CpSolver()` and call back the solution found for each block of the Magic Square. From a list of all n<sup>2</sup> variables, split the list into equal sections of 9 values using the `equal_parts` method created, and output each row to generate the completed Magic Square.
    * _Provide runtime statistics_ - The program provides the user with insight to the program by outputting the status, the number of conflicts, the number of search branches, the time the program took to complete, and the total number of solutions found.

* <a href='https://github.com/amar-sinha/or-tools/tree/master/N-Queens'>_N-Queens_</a> - The N-Queens Solver takes a number _n_ as user input. The program solves the puzzle by finding placements of the _n_ queens on an _n_ x _n_ chessboard such that no two queens are threatening each other.

* <a href='https://github.com/amar-sinha/or-tools/tree/master/Sudoku%20Solver'>_Sudoku Solver_</a> - The Sudoku Solver takes a 9x9 Sudoku puzzle as user input. The user enters nine rows and nine columns of values separated by spaces, where blank spaces are entered as 0 and preset spaces are entered as the given number. 
    * _Create a matrix of all variables_ - The program first creates uniquely identified NewIntVar integer variables and organizes them in a 9x9 NumPy matrix.
    * _Define and add constraints_ - The `AddAllDifferent` constraint is applied to the Sudoku puzzle to fill unique values of 1-9 in each row, column, and 3x3 subsquare. To add each constraint:
        * _Rows_ - iterate through each row of the matrix stored as a NumPy array to add each row constraint
        * _Columns_ - iterate through each row of the transpose of the matrix (i.e. the columns of the original matrix) stored as a NumPy array to add each column constraint
        * _Subsquares_ - iteratively create 3x3 slices for each subsquare in each three-row set and three-column set and add each subsquare constraint
    * _Generate and call the solution_ - Generate the solution using `cp_model.CpSolver()` and call back the solution found for each block of the Sudoku puzzle. From a list of all 81 variables, split the list into equal sections of 9 values using the `equal_parts` method created, and output each row to generate the completed Sudoku Puzzle.
    * _Provide runtime statistics_ - The program provides the user with insight to the program by outputting the status, the number of conflicts, the number of search branches, the time the program took to complete, and the total number of solutions found.