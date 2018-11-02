from random import randint

x = 10
n = 0
while n < x:
    r_num = randint(0,5)    # converts to 1-6
    dot ='o '
    s = '-----\n|' + dot[r_num < 1] + ' ' + dot[r_num < 3] + '|\n|' + dot[r_num < 5]
    print(s + dot[r_num&1] + s[::-1])

    #print('+' * 10)
    #print(r_num)

    # if FALSE=first char; if TRUE=second char
    #print(r_num < 1)
    #print(r_num < 3)
    #print(r_num < 5)
    #print(dot[r_num < 1])
    #print(dot[r_num < 3])
    #print(dot[r_num < 5])

    #print('print string: \n%s' % s)
    #print('print middle dot: %s' % dot[r_num&1])
    #print('print reverse string: \n%s' % s[::-1])

    n += 1