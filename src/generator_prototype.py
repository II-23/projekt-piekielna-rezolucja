from tools import Formula, Variable, And, Or, Not
from random import choice, randint

letters = ['p','q','r','s','t','u','w']
# letters = ['p','q','r']

# def generate_formula(letters):
#     while True: 
#         x, y = [choice(letters), randint(0,1)], [choice(letters), randint(0,1)] #choice first variable and its sign, choice seciund -||-
#         if x[0]==y[0]: continue
#         x_var = Not(Variable(x[0])) if x[1]==0 else Variable(x[0])
#         y_var = Not(Variable(y[0])) if y[1]==0 else Variable(y[0])
#         chance = randint(0,100)
#         if chance>=0:
#             z = [choice(letters), randint(0,1)]
#             if z[0]==x[0] or z[0]==y[0]: continue
#             z_var = Not(Variable(z[0])) if z[1]==0 else Variable(z[0])
#             formula = Or(Or(x_var,y_var),z_var)
#         else:
#             formula = Or(x_var,y_var)
#         if formula.tautology() or Not(formula).tautology():
#                 continue
#         return formula
    
def generate_variable(letters):
    return Variable(choice(letters))

def derive_formulas(letters, formula, letter=None):
    #takes a formula and returns two formulas whose 'formula' is the resolvent

    if len(formula.used_variables()) == 1:
        if not letter:
            letter = choice(letters)
            while letter in formula.used_variables():
                letter = choice(letters)
        x = Variable(letter)
        y = Not(Variable(letter))
        order = randint(1,4)
        if order==1: return (Or(x, formula), Or(y, formula))
        if order==2: return (Or(formula, x), Or(formula, y))
        if order==3: return (Or(x, formula), Or(formula, y))
        if order==4: return (Or(formula, x), Or(y, formula))

    if len(formula.used_variables()) == 2:
            f1 = formula.formula1
            f2 = formula.formula2

            if not letter:
                letter = choice(letters)
                while letter in formula.used_variables():
                    letter = choice(letters)

            type_ = randint(2,3)

            if type_ == 2:
                x = Variable(letter)
                y = Not(Variable(letter))
                order = randint(1,4)
                if order==1: return (Or(x, f1), Or(y, f2))
                if order==2: return (Or(f1, x), Or(f2, y))
                if order==3: return (Or(x, f1), Or(f2, y))
                if order==4: return (Or(f1, x), Or(y, f2))

            if type_ == 3:
                chance = randint(0,2)
                new = Variable(letter)
                if chance==0:
                    chance = randint(0,1)
                    if chance:
                        x = Or(Or(f1, f2), new)
                        y = Or(Not(new), choice((f1,f2)))
                    else: 
                        x = Or(Or(f1, f2), Not(new))
                        y = Or(new, choice((f1,f2)))

                if chance==1:
                    chance = randint(0,1)
                    if chance:
                        x = Or(f1, Or(new, f2))
                        y = Or(Not(new), choice((f1,f2)))
                    else: 
                        x = Or(Or(f2, Not(new)), f1)
                        y = Or(new, choice((f1,f2)))

                if chance==2:
                    chance = randint(0,1)
                    if chance:
                        x = Or(Or(new, f1), f2)
                        y = Or(choice((f1,f2)), Not(new))
                    else: 
                        x = Or(Or(f1, Not(new)), f2)
                        y = Or(choice((f1,f2)), new)

                return (x,y)
                         
    if len(formula.used_variables()) == 3:
            if len(formula.formula1.used_variables())==1: f1, f2, f3 = formula.formula1, formula.formula2.formula1, formula.formula2.formula2
            else: f1, f2, f3 = formula.formula1.formula1, formula.formula1.formula2, formula.formula2
            return (f1,f2,f3)

x=derive_formulas(letters, Or(Variable('p'), Variable('r')))
for i in x:
      print(i)
# print(x)

# print(choice([1,2]))


# class Set_formulas_n:
#     def __init__(self, size, letters):
#         self.size=size
#         self.letters=letters
#         self.set = []

#     def clear(self):
#         self.set=[]
    
#     def clear_one(self, index):
#         self.set.pop(index)

#     def fill(self):
#         for _ in range(self.size):
#             while True:
#                 formula = generate_formula(self.letters)
#                 self.set.append(formula)
#                 break

#     def chceck(self):
#         ...
            
# size = 5
# x = Set_formulas_n(size,letters)
# x.fill()
# for i in range(size):
#     print(x.set[i])

# print(generate_variable(letters))