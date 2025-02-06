A,B = map(int, input().split())
C,D = map(int, input().split())
E,F = map(int, input().split())

x = A
y = B
if x == C: x = E
elif x == E: x = C
    
if y == D: y = F
elif y == F: y = D

print(x,y)
