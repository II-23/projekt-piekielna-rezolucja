from random import *

max_variable_number=5
formulas_number=5
max_len=4
formula_choice_modifier=0.3
variable_choice_modifier=0.5

CHANCE_FOR_SATISFIABLE = 100 # as a percentage


class Formula:
    def __init__(self, max_variable_number):
        self.length = 0 # how many varibales are initialized in the formula
        self.variables=[] # every element is linked to a variable; -1 = the variable is in negation; 1 = the variable is NOT in negation; 0 - the variable is NOT present in the formula
        self.size = max_variable_number # how many variables can there be in the formula
        for i in range(self.size):
            self.variables.append(0)

class Set_Of_Formulas:
    def __init__(self, size, max_variable_number):
        self.table = [] # stores the list of formulas
        self.size = size # how many formulas are there in the set
        self.satisfiable = True # True = the set is satisfiable, False = the set is NOT satisfiable
        self.valuation = [] # every element in the list is linked to a variable; 1 = the variable has to have value true; -1 = the variable has to have value false; 0 = the variable can have any value; if self.satisfiable is False then self.valuation is all 0's
        for i in range(self.size):
            self.table.append(Formula(max_variable_number))
        for i in range(max_variable_number):
            self.valuation.append(0)

    def fill(self, max_len):
        satisfiable = randint(0, 100) # drawing whether the set of formulas will be satisfiable
        if satisfiable <= CHANCE_FOR_SATISFIABLE:
            self.satisfiable == True
            
            valuated = [False for i in range(len(self.valuation))]
            # generating formulas
            for formula in self.table:
                initialized = [False for i in range(len(self.valuation))]
                var = randint(0, len(self.valuation) - 1)
                if valuated[var] == False:
                    self.valuation[var] = choice([-1, 1])
                    valuated[var] = True
                formula.variables[var] = self.valuation[var]
                formula.length = 1
                initialized[var] = True
                length = randint(1, max_len)
                while formula.length < length:
                    while initialized[var] == True:
                        var = randint(0, formula.size - 1)
                    formula.variables[var] = choice([-1, 1])
                    formula.length += 1
                    initialized[var] = True
        else:
            self.satisfiable = False
                            



                

'''
def generate(max_variable_number, formulas_number, max_len, base):        
        #adding an empty formula as a base on which other formulas will be formed
        set_of_formulas = Set_Of_Formulas(max_variable_number)
        while len(set_of_formulas) < formulas_number:
            modified_formula_id = randint(0, len(set_of_formulas) - 1)
            modified_formula = set_of_formulas[modified_formula_id]
            set_of_formulas.pop(modified_formula_id)
            if modified_formula[0] == max_len:
                continue
            chosen_variable = randint(0, max_len - modified_formula[0] - 1)
            for i in range(chosen_variable):
                if (modified_formula[1][chosen_variable] != 0):
                    i -= 1
            modified_formula[1][chosen_variable] -= 1
            set_of_formulas.append(modified_formula)
            modified_formula[1][chosen_variable] += 2
            set_of_formulas.append(modified_formula)
'''    

abc = Set_Of_Formulas(formulas_number, max_variable_number)   
abc.fill(max_len)        
        
print(f"{abc.size}, , {abc.satisfiable}, {abc.valuation}")
for formula in abc.table:
    print(f"{formula.size}, {formula.variables}, {formula.length}")
"""
generate(max_variable_number, formulas_number, max_len)
Function returns list of lists. These lists represent formulas and list of lists represents set of formulas given to a player.
In any given list 0 should be interpreted as variable not in formula, 1 as variable in formula and -1 as variables negation in formula.
If both var and its negation are in formula because of players mistake i suggest 2. 
Function prioritizes shorter formulas to be "complicated", with each next length of formula beeing less likely by the factor of formula_choice_modifier.
"""