def get_num(board,i,j):
    cnt = 0
    predict = 'B'
    
    for r in range(i,i+8):
        for c in range(j,j+8):
            bw = board[r][c]
            
            if predict != bw:
                cnt += 1

            if c == j+7:
                break
                
            elif predict == 'B': 
                predict = 'W'
            else: 
                predict ='B'

    predict = 'W'
    cnt2 = 0
    for r in range(i,i+8):
        for c in range(j,j+8):
            bw = board[r][c]
            
            if predict != bw:
                cnt2 += 1

            if c == j+7:
                break
                
            elif predict == 'B': 
                predict = 'W'
            else: 
                predict ='B'
                
    if cnt > cnt2:
        return cnt2
    return cnt
    
    
N, M = map(int, input().split())
board = []

for i in range(N):
    b = input()
    board.append(b)

min_num = 100
for i in range(0, N-7):
    for j in range(0, M-7):
        tmp = get_num(board, i, j)
        if tmp < min_num:
            min_num = tmp
print(min_num)