import random

def game(comp,user):
    if comp == user:
        print('match tied')
    elif comp == 's':
        if user == 'w' or user == 'g':
            print('User Win')
    elif comp == 'w':
        if user == 'g' or user == 's':
            print('Comp Win')
    elif comp == 'g':
        if user == 'w':
            print('User Win')
        elif user == 's':
            print('Comp Win' )   
    print("computer selected ",comp ," you aelected ",user)
    



print('Computer have selected you have to select...')

random_No = random.randint(1,3)

if random_No == 1:
    comp ='s'
elif random_No == 2:
    comp = 'w'
elif random_No == 3:
    comp = 'g'
 
user = input('Snake(s) Water(w) Gun(g)')

game(comp,user)