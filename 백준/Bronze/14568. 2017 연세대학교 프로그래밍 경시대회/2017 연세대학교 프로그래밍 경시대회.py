N = int(input())
count = 0

for c in range(2, N, 2):
    
    b = int((N-c)/2)-1
    if b > 0: count = (int((N-c)/2)-1) + count
    
print(count)