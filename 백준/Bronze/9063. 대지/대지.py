N = int(input())
min_x = 10001
max_x = -10001
min_y = 10001
max_y = -10001

for i in range(N):
    X, Y= map(int, input().split())
    
    if X > max_x: max_x = X
    if X < min_x: min_x = X
    if Y > max_y: max_y = Y
    if Y < min_y: min_y = Y
print((max_x - min_x)*(max_y - min_y))