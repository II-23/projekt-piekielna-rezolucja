from random import *

CHANCE_FOR_SATISFIABLE = 100 # as a percentage

max_variable_number= 5
formulas_number=5 # has to be at least 2
max_len=4 # has to be lower than max_variable_number

"""
class Formula
    stores:
        - [int] length - the number of set variables in the Formula
        - [int] size - the maximum number of variables which the formula can hold; size = max_variable_number
        - [list] variables - content of the formula; variables[i] == 0 means i'th variable is not in the formula /
        variables[i] == -1 means i'th variable is in negation / variables == 1 means i'th variable is not in negation

    does:
        - __init__ - creates an empty formula with length = 0, variables = [0,0,...,0] and size = len(variables) = max_variable_number
        - clear - sets length to 0 and variables to all zeroes form [0,0,...,0]
        - copies formula as is [returns class Formula object - the copy of self]

class Set_Of_Formula
    stores:
        - [int] size - the number of formulas in the set
        - [bool] satisfiable - True if set is satisfiable, False otherwise
        - [list] formulas - list of class Formula objects which hold formulas in the set
        - [list] valuation - example of correct valuation; valuation[i] == 1 - i'th variable is true, valuation[i] == -1 - i'th variable is false, valuation[i] == 0 - value of i'th variable can be both true and false

    does:
        - __init__ - creates an empty set with size = formulas_number, satisfiable = False, formulas = list of size = formulas_number storing empty class Formula objects whose sizes are set to max_variable_number], valuation - [0,0,...,0]
        - clear - sets all attributes of a set to initial values as in __init__
        - fill - according to CHANCE_OF_SATISFIABLE generates either satisfiable or contradictory sets of formulas
"""


class Formula:
    def __init__(self, max_variable_number):
        self.length = 0 # how many varibales are initialized in the formula
        self.variables=[] # every element is linked to a variable; -1 = the variable is in negation; 1 = the variable is NOT in negation; 0 - the variable is NOT present in the formula
        self.size = max_variable_number # how many variables can there be in the formula
        for i in range(self.size):
            self.variables.append(0)

    def clear(self):
        self.length = 0;
        for i in range(len(self.variables)):
            self.variables[i] = 0
    
    def copy(self):
        formula_copy = Formula(self.size)
        formula_copy.length = self.length
        formula_copy.variables = self.variables.copy()
        return formula_copy


class Generator:
    def __init__(self, size, max_variable_number):
        self.formulas = [] # stores the list of formulas
        self.size = size # how many formulas are there in the set
        self.satisfiable = True # True = the set is satisfiable, False = the set is NOT satisfiable
        self.valuation = [] # every element in the list is linked to a variable; 1 = the variable has to have value true; -1 = the variable has to have value false; 0 = the variable can have any value; if self.satisfiable is False then self.valuation is all 0's
        for i in range(self.size):
            self.formulas.append(Formula(max_variable_number))
        for i in range(max_variable_number):
            self.valuation.append(0)

    def clear(self):
        for formula in self.formulas:
            formula.clear
        self.satisfiable = False
        for i in range(len(self.valuation)):
            self.valuation[i] = 0
            
    def fill(self, max_len, max_variable_number):
        self.clear()
        satisfiable = randint(0, 100) # drawing whether the set of formulas will be satisfiable
        #generating safisfiable sets
        if satisfiable <= CHANCE_FOR_SATISFIABLE: 
            self.satisfiable == True
            valuated = [False for i in range(len(self.valuation))] # keeps track of whether value of certain variable has been generated
            # generating formulas
            for formula in self.formulas:
                initialized = [False for i in range(len(self.valuation))]
                var = randint(0, len(self.valuation) - 1)
                if valuated[var] == False: # if drawn variable has not yet been set. Then choose a value for it
                    self.valuation[var] = choice([-1, 1])
                    valuated[var] = True
                formula.variables[var] = self.valuation[var]
                formula.length = 1
                initialized[var] = True
                length = randint(1, max_len) # drawing a length of the current formula
                while formula.length < length:
                    while initialized[var] == True: 
                        var = randint(0, formula.size - 1) # drawing a variable to initialize from those which have not yet been initialized
                    formula.variables[var] = choice([-1, 1])
                    formula.length += 1
                    initialized[var] = True
            # at the end Set_Of_Formulas.formulas stores the set of formulas which can be satisfied by the Set_Of_Formulas.valuation. Keep in mind that .valuation is not the only correct valuation and the .valuation[i] has value 0 if i'th variable may either be True or False
            return
        else: # creating contradictory sets
            self.satisfiable = False
            vars = [i for i in range(max_variable_number)]
            formulas = []
            formulas.append(Formula(max_variable_number))
            while len(vars) > 0:
                modified_formula = choice(formulas)
                if modified_formula.length == max_len:
                    continue
                var = choice(vars)
                vars.remove(var)
                backlog = randint(0, max(0, modified_formula.length))
                modified_formula_cut = modified_formula.copy()
                initialized = []
                for i in range(modified_formula.size):
                    if modified_formula.variables[i] != 0:
                        initialized.append(i)
                while backlog > 0:
                    backlog -= 1
                    id = choice(initialized)
                    initialized.remove(id)
                    modified_formula_cut.variables[id] = 0
                    modified_formula_cut.length -= 1
                modified_formula.variables[var] = choice([-1, 1])
                modified_formula.length += 1
                modified_formula_cut.variables[var] = -1 * modified_formula.variables[var]
                modified_formula_cut.length += 1
                formulas.append(modified_formula_cut)
            self.formulas = formulas

        # returns a list of lists according to a specification given at the bottom of this document
        def get_list_of_lists(self):
            list_of_lists = []
            for formula in self.formulas:
                list_of_lists.append([formula.length, formula.variables])
            return list_of_lists




"""DEMO"""


def generate(max_variable_number, formulas_number, max_len):
    formulas = Generator(formulas_number, max_variable_number)
    formulas.fill(max_len, max_variable_number)
    return formulas.get_list_of_lists()

abc = Generator(formulas_number, max_variable_number)   
abc.fill(max_len, max_variable_number)        
        
print(f"Size of set:{abc.size}\nSatisfiable?: {abc.satisfiable}\nExample of correct valuation:\n{abc.valuation}\nFormulas:")
for formula in abc.formulas:
    print(f"Formula: {formula.variables}, Length: {formula.length}")
