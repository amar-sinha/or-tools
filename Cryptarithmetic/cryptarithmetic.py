from __future__ import print_function
from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    ## Print intermediate solutions

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
word on a newline. For n words, all words up to
the (n-1)th word will sum to equal the nth word.""")

    word_array = []
    split_word_array = []
    letters = []
    
    while True:
        word = input()
        if word:
            word_array.append(word)
            split_word = split_string(word)
            split_word_array.append(split_word)
            
            for char in split_word:
                if char not in letters:
                    letters.append(char)
        else:
            break
    
    print(word_array)
    print(letters)
    print(split_word_array)

if __name__ == "__main__":
    cryptarithmetic()