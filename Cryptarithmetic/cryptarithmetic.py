from __future__ import print_function
from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    # Print intermediate solutions

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


def split_string(str):
    return [char for char in str]


def cryptarithmetic():
    # Constraint programming engine
    model = cp_model.CpModel()

    print(
        """Enter any number of words by entering each
word on a new line. For n words, all words up to
the (n-1)th word will sum to equal the nth word.""")

    word_array = []
    split_word_array = []
    letters_dict = {}

    while True:
        word = input()
        if word:
            word_array.append(word)
            split_word = split_string(word)
            split_word_array.append(split_word)
        else:
            break

    base = 10

    # Generate NewIntVars for each unique letter
    for word in split_word_array:
        for char in word:
            if char not in letters_dict:
                if word.index(char) == 0:
                    letters_dict[char] = model.NewIntVar(1, base-1, char.upper())
                else:
                    letters_dict[char] = model.NewIntVar(0, base-1, char.upper())
    
    intvar_array = letters_dict.values()

    # Make sure there are enough digits
    assert base >= len(intvar_array)

    # Generate string version of equation
    lhs = " + ".join(word_array[:len(word_array)-1]) 
    rhs = " = " + word_array[len(word_array)-1]
    equation = lhs.upper() + rhs.upper() + "\n"
    
    print(equation)

    # Compute the equation
    constraint_array = []
    for word in split_word_array:
        exp = len(word)-1
        value = 0
        for char in word:
            value += letters_dict[char] * pow(base, exp)
            exp -= 1
        constraint_array.append(value)
    
    constraint_lhs = sum(constraint_array[:len(constraint_array)-1])
    constraint_rhs = constraint_array[len(constraint_array)-1]

    # Define constraints
    model.AddAllDifferent(intvar_array)
    model.Add(constraint_lhs == constraint_rhs)

    # Solve model
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter(intvar_array)
    status = solver.SearchForAllSolutions(model, solution_printer)

    print()
    print('Statistics')
    print('  - status          : %s' % solver.StatusName(status))
    print('  - conflicts       : %i' % solver.NumConflicts())
    print('  - branches        : %i' % solver.NumBranches())
    print('  - wall time       : %f s' % solver.WallTime())
    print('  - solutions found : %i' % solution_printer.solution_count())


if __name__ == "__main__":
    cryptarithmetic()