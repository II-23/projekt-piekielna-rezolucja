from random import *

max_variable_number=5
formulas_number=5
max_len=4
formula_choice_modifier=0.3
variable_choice_modifier=0.5
def empty(x):
    z=[]
    for i in range(x):
        z.append(0)
    return z
def generate(max_variable_number, formulas_number, max_len, formula_choice_modifier):
    table=[]
    #add list consisting of number of variables and "tuple" of values of vars
    table.append([0, empty(max_variable_number)])
    while len(table)<formulas_number:
        sum=0
        #calculating total weight of all formulas
        for x in table:
            sum+=1000*formula_choice_modifier**x[0]
        y=randint(0,10000)/10000
        sum2=0
        index=0
        while sum2/sum<y:
            sum2+=1000*formula_choice_modifier**table[index][0]
            index+=1
        index=index-1
        if table[index][0]==max_len:
            continue
        #we found weighted and randomised choice of formula to complicate
        to_complicate=table[index]
        choice_to_complicate=[]
        for i in range(len(to_complicate[1])):
            if to_complicate[1][i]==0:
                choice_to_complicate.append(i)
        if len(choice_to_complicate)==0:
            continue
        #we created a list of variables we can shove into our selected formula. Next step is to make a choice which one
        '''existing_vars=empty(max_variable_number)
        tier=table[index][0]+1
        for x in table:
            if x[0]==tier:
                for i in range(len(x)):
                    if x[1][i]!=0:
                        existing_vars[i]+=1
        print(existing_vars)'''
        x=choice(choice_to_complicate)
        q1=[to_complicate[0]+1, to_complicate[1].copy()]
        q2=[to_complicate[0]+1, to_complicate[1].copy()]
        q1[1][x]=1
        q2[1][x]=-1
        table.append(q1)
        table.append(q2)
        table.pop(index)
    return(table)
                    
        
print(generate(max_variable_number, formulas_number, max_len, formula_choice_modifier))
"""
Function returns list of lists. These lists represent formulas and list of lists represents set of formulas given to a player.
In any given list 0 should be interpreted as variable not in formula, 1 as variable in formula and -1 as variables negation in formula.
If both var and its negation are in formula because of players mistake i suggest 2. 
Function prioritizes shorter formulas to be "complicated", with each next length of formula beeing less likely by the factor of formula_choice_modifier.
"""