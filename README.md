# Google OR-Tools
## Constraint Programming

_<h4>Project implementations utilizing the Google OR-Tools packages for constraint programming.</h4>_

### <u>Goal</u>


### <u>Package Installation</u>
Install ortools

    $ python -m pip install --upgrade --user ortools

Install numpy

    $ pip install numpy

### <U>Project Descriptions</u>
* _Sudoku Solver_ - The Sudoku Solver takes a 9x9 Sudoku puzzle as user input. The user enters nine rows and nine columns of values separated by spaces, where blank spaces are entered as 0 and preset spaces are entered as the given number. 
    * _Create a matrix of all variables_ - The program first creates uniquely identified NewIntVar integer variables and organizes them in a 9x9 NumPy matrix.
    * _Define and add constraints_ - The constraints on a Sudoku puzzle are to have unique values of 1-9 in each row, column, and 3x3 subsquare. 