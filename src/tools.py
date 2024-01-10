from itertools import product
from random import choice

'''Może dużo tekstu, ale od 160 linijki są testy więc nie ma aż tak dużo'''

class MissingVariableValue(Exception):
    ...

class IncorrectVariableValue(Exception):
    ...

class IncorrectConstantValue(Exception):
    ...

class ArgumentError(Exception):
    ...

class Formula:
    def __init__(self):
        ...
    def __add__(self, other):
        return Or(self, other)
    def __mul__(self, other):
        return And(self, other)

    def used_variables(self):
        variables_set = set()
        if isinstance(self, Variable): variables_set.add(self.variable)
        if isinstance(self, And) or isinstance(self, Or): 
            variables_set.update(self.formula1.used_variables())
            variables_set.update(self.formula2.used_variables())
        if isinstance(self, Not):
            variables_set.update(self.formula.used_variables())
        return variables_set

    def tautology(self):
        if isinstance(self, Constant):
            return self.constant
        variables_set = self.used_variables()
        for c in product([True,False], repeat=len(variables_set)):
            new = dict(zip(variables_set, c))
            if not self.calculate(new):
                return False
        return True
    
    def generate(letters):
        return Or(Variable(choice(letters)), Variable(choice(letters)))
    


class Variable(Formula):
    def __init__(self,variable):
        self.variable = variable

    def simplify(self):
        return Variable(self.variable)

    def calculate(self, variables):
        return variables[self.variable]
    
    def __str__(self):
        return f'{self.variable}'
    
    def __eq__(self, other):
        return self.variable == other.variable
    
class Constant(Formula):
    def __init__(self, constant):
        self.constant = constant

    def calculate(self, variables):
        return self.constant
    
    def __str__(self):
        return str(self.constant)

    def __eq__(self, other):
        return self.constant == other.constant
    
    
class And(Formula):
    def __init__(self, formula1, formula2):
        self.formula1 = formula1
        self.formula2 = formula2
        
    def calculate(self, variables):
        '''Warning! The formula (p ∧ False) is always False, even if "variables" does not contain p. 
        This is because (x ∧ False) is a contradiction.'''
        return self.formula1.calculate(variables) + self.formula2.calculate(variables) == 2
    
    def __str__(self):
        return f'({self.formula1} ∧ {self.formula2})'
    
    def __eq__(self, other):
        return {self.formula1, self.formula2} == {other.formula1, other.formula2}


class Or(Formula):
    def __init__(self, formula1, formula2):
        self.formula1 = formula1
        self.formula2 = formula2

    def calculate(self, variables):
        return self.formula1.calculate(variables) + self.formula2.calculate(variables) > 0
    
    def __str__(self):
        return f'({self.formula1} v {self.formula2})'
    
    def __eq__(self, other):
        return {self.formula1, self.formula2} == {other.formula1, other.formula2}

class Not(Formula):
    def __init__(self, formula):
        self.formula = formula

    def calculate(self, variables):
        return True if self.formula.calculate(variables) == False else False
    
    def __str__(self):
        return f'~{self.formula}'
    
    def __eq__(self, other):
        return self.formula == other.formula

# variables = {

#                 'p': True,
#                 'q': False,
#                 'r': True,
#                 's': False,
#                 'x': True,
#                 'y': False,
#                 'j': 'true'}
    

