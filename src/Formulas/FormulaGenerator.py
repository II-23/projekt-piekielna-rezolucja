from random import *

CHANCE_FOR_SATISFIABLE = 30 # as a percentage

"""
USAGE:
To generate a set of fomulas create an object Generator, which takes
"""


"""
max_variable_number - how many distinct variables are there
max_len - maximum length a single formula can have
formulas_number - how many formulas are there in a set

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
        - __init__ - creates an empty set with sets max_variable_number, max_len and number of formulas according to difficulty.
        Draws whether a set will be satisfiable or not. Then calls fill
        - fill - generates formulas with full type tree - medium and hard levels
        - fill_simple - generates easy contradictory sets with tree-like resolution structure
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
    def __init__(self, difficulty):
        satisfiable = (randint(0, 100) <= CHANCE_FOR_SATISFIABLE)
        print(satisfiable)
        if difficulty == 1:
            max_variable_number = 4
            formulas_number = 4
            max_len = 3
        elif difficulty == 2:
            max_variable_number = 5
            formulas_number = 6
            max_len = 4
        elif difficulty == 3:
            max_variable_number = 6
            formulas_number = 7
            max_len = 5
        else:
            max_variable_number = 7
            formulas_number = 8
            max_len = 6
        
        self.formulas = [] # stores the list of formulas
        self.size = formulas_number # how many formulas are there in the set
        self.satisfiable = satisfiable # True = the set is satisfiable, False = the set is NOT satisfiable
        self.valuation = [] # every element in the list is linked to a variable; 1 = the variable has to have value true; -1 = the variable has to have value false; 0 = the variable can have any value; if self.satisfiable is False then self.valuation is all 0's
        for i in range(self.size):
            self.formulas.append(Formula(max_variable_number))
        for i in range(max_variable_number):
            self.valuation.append(0)
        if difficulty == 1:
            self.fill_simple(satisfiable, max_len, max_variable_number)
        else:
            self.fill(satisfiable, max_len, max_variable_number)

    def clear(self):
        for formula in self.formulas:
            formula.clear()
        self.satisfiable = False
        for i in range(len(self.valuation)):
            self.valuation[i] = 0

    def fill_simple(self, satisfiable, max_len, max_variable_number):
        if satisfiable: 
            self.fill(satisfiable, max_len, max_variable_number)
        else:
            vars = [i for i in range(max_variable_number)]
            formulas = []
            formulas.append(Formula(max_variable_number))
            while len(vars) > 0:
                if len(formulas) == self.size:
                    break
                modified_formula = choice(formulas)
                if modified_formula.length == max_len:
                    continue
                var = choice(vars)
                vars.remove(var)
                modified_formula_new = modified_formula.copy()
                modified_formula.variables[var] = choice([-1, 1])
                modified_formula.length += 1
                modified_formula_new.variables[var] = -1 * modified_formula.variables[var]
                modified_formula_new.length += 1
                formulas.append(modified_formula_new)
            self.formulas = formulas



    def fill(self, satisfiable, max_len, max_variable_number):
        # drawing whether the set of formulas will be satisfiable
        #generating safisfiable sets
        if satisfiable: 
            var_used = [[0,0] for i in range(max_variable_number)] # keeps track of whether value of certain variable has been generated
            # generating formulas
            for i in range(len(self.valuation)): # drawing value for each variable
                self.valuation[i] = choice([-1, 1])
                var_used[i][0] = 0 # how many times a variable has been used in the whole set
                var_used[i][1] = 0 # what is the advantage for the variable (how many more times has this variable been used in the positive (+1)vs negation (-1) form)

            used_to_satisfy = [False for i in range(max_variable_number)] # to ensure that one variable is not used to provide satisfiability for more than one set. After that is it up to the advantage mechanic to ensure that one variable does not occure in the same state to frequently in the set

            for formula in self.formulas:
                # draw a variable which provides satisfiabilty
                sat_var = randint(0, formula.size - 1)
                if False in used_to_satisfy:
                    while used_to_satisfy[sat_var] == True:
                        sat_var = randint(0, formula.size - 1)

                initialized = [False for i in range(max_variable_number)]
                initialized[sat_var] = True
                used_to_satisfy[sat_var] = True
                var_used[sat_var][0] += 1
                var_used[sat_var][1] += self.valuation[sat_var]
                formula.variables[sat_var] = self.valuation[sat_var]
                formula.length += 1
                length = randint(1, max_len) # drawing a length of the current formula
                while formula.length < length:
                    var = 0;
                    final_var = True;
                    while final_var: 
                        var = randint(0, formula.size - 1) # drawing a variable to initialize from those which have not yet been initialized
                        final_var = var_used[var][0] <= max(2, self.size - max_variable_number + 1) and initialized[var] == True

                    # to ensure that a single variable is not responsible for to many formulas satisfiability
                    if var_used[var][1] > 0:
                        formula.variables[var] = -1
                        var_used[var][1] -= 1 # beacuse self.valuation[var] is either -1 or 1 then var_used[self.val...] will result in either var_used[1] or var_used[-1] == var_used[2] accordingly
                    else:
                        formula.variables[var] = 1
                        var_used[var][1] += 1
                    formula.length += 1
                    var_used[var][0] += 1
                    initialized[var] = True
            # at the end Set_Of_Formulas.formulas stores the set of formulas which can be satisfied by the Set_Of_Formulas.valuation. Keep in mind that .valuation is not the only correct valuation and the .valuation[i] has value 0 if i'th variable may either be True or False
            return
        else: # creating contradictory sets
            vars = [i for i in range(max_variable_number)]
            formulas = []
            formulas.append(Formula(max_variable_number))
            while len(vars) > 0:
                if len(formulas) == self.size:
                    break
                modified_formula = choice(formulas)
                if modified_formula.length == max_len:
                    continue
                var = choice(vars)
                vars.remove(var)
                backlog = randint(0, max(0, modified_formula.length // 2 - max_variable_number // 2))
                modified_formula_new = modified_formula.copy()
                if (modified_formula.length >= 0):
                    initialized = []
                    for formula in formulas:
                        print(formula.variables)
                    cnts = [1 for i in range(max_variable_number)]
                    for i in range(max_variable_number):
                        if modified_formula.variables[i] != 0:
                            for formula in formulas:
                                if formula.variables[i] != 0:
                                    cnts[i] *= 2

                    for c in range(len(cnts)):
                        if cnts[c] > 1:
                            for i in range(cnts[c]):
                                initialized.append(c)

                    modified_formulas = [modified_formula_new, modified_formula]
                    while backlog > 0 or len(initialized) != 0:
                        backlog -= 1
                        id = choice(initialized)
                        for i in range(initialized.count(id)):
                            initialized.remove(id)
                        which_one = choice([0, 1])
                        modified_formulas[which_one].variables[id] = 0
                        modified_formulas[which_one].length -= 1

                modified_formula.variables[var] = choice([-1, 1])
                modified_formula.length += 1
                modified_formula_new.variables[var] = -1 * modified_formula.variables[var]
                modified_formula_new.length += 1
                formulas.append(modified_formula_new)
            self.formulas = formulas


if __name__ == "__main__":
    difficulty = 4
    abc = Generator(difficulty)          
    print(f"Size of set:{abc.size}\nSatisfiable?: {abc.satisfiable}\nExample of correct valuation:\n{abc.valuation}\nFormulas:")
    for formula in abc.formulas:
        print(f"Formula: {formula.variables}, Length: {formula.length}")
