N = int(input())

#흰 도화지 배열
draw = [[0 for i in range(100)] for j in range(100)]

# 색종이 붙이기
for i in range(N):
    x,y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            draw[x+j][y+k] = 1
# 넓이
count = 0
for i in range(100):
    for j in range(100):
        if draw[i][j] == 1:
            count += 1
print(count)