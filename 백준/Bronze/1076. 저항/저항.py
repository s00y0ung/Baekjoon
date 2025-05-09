resistance = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4
    ,'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

c1 = input()
c2 = input()
c3 = input()
print(resistance[c1]*(10 ** (1+resistance[c3])) +  resistance[c2] * (10 ** resistance[c3]))