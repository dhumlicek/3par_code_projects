from random import randint

def diceRoll():
    x = 0
    roll_total = 0
    while x < 2:
        r_num = randint(0,5)
        dot ='o '
        s = '-----\n|' + dot[r_num < 1] + ' ' + dot[r_num < 3] + '|\n|' + dot[r_num < 5]
        print(s + dot[r_num&1] + s[::-1])
        roll_total += (r_num + 1)
        x += 1

    return roll_total


def validateNum(user_num):
    try:
        number = int(user_num)
        if number > 0:
            print("Rolling the dice %s times...\n\n" % number)
            flag = True
            return number, flag
        else:
            print("Please enter a positive integer")
            flag = False
            number = None
            return number, flag
    except ValueError:
        print("I am afraid %s is not a positive integer" % user_num)
        flag = False
        number = None
        return number, flag


val = False
while val == False:
    unum = input("How many times do you want to roll the dice? \n (HINT: each roll is a pair of dice) : ")
    valnum, val = validateNum(unum)
    #print(valnum)
    #print(val)
    
n = 0
total = 0
full_total = 0

while n < valnum:

    print("-"*15," Dice roll: %s" % (n + 1))
    total = diceRoll()
    print("\nDice roll total: %s" % total)
    full_total += total
    n += 1

print("-"*15,"\n\nRolled dice %s times.\nTotal Roll amount : %s" % (valnum, full_total))