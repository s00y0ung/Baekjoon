from copy import deepcopy
def InWorm(c_list, w_list, row, col, width, height):
    stack = [(row, col)]
    
    while len(stack) != 0:
        row,col = stack.pop()
        w_list[row][col] = 1
        
        if row+1 < height: # down
            if c_list[row+1][col] == 1 and w_list[row+1][col] == 0: 
                stack.append((row+1, col))
    
        if col+1 < width: # right
            if c_list[row][col+1] == 1 and w_list[row][col+1] == 0: 
                stack.append((row, col+1))
                
        if row-1 >= 0: # up
            if c_list[row-1][col] == 1 and w_list[row-1][col] == 0: 
                stack.append((row-1,col))
                
        if col-1 >= 0: # left
            if c_list[row][col-1] == 1 and w_list[row][col-1] == 0: 
                stack.append((row, col-1))

test_cnt = int(input())

for _ in range(test_cnt):
    width, height, k = map(int, input().split())
    cabbage = []
    worm = []
    worm_cnt = 0
    
    # 배추밭 만들기
    for i in range(height):
        c_list = []
        for j in range(width):
            c_list.append(0)
        cabbage.append(c_list)
    worm = deepcopy(cabbage)
        
    # 배추 심기
    for i in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
        
    # 지렁이 
    for i in range(height):
        for j in range(width):
            if cabbage[i][j] == 1 and worm[i][j] == 0:
                worm_cnt += 1
                InWorm(cabbage, worm, i, j, width, height)
    print(worm_cnt)