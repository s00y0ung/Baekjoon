def find(a,depth,n,col):
    global N, ans,ans_arr
    if depth == n:
        if ans == N:
            for s in a:
                print(s,end='')
        ans = ans-1
        return 0

    for i in range(col,-1,-1):
        a.append(i)
        find(a,depth+1,n,i-1)
        a.pop(-1)

N = int(input())

count = [[0]*10, [1]*10]
prefix = [[0]*10,[i for i in range(10)]]

for i in range(2,11):
    count.append([-1]*10)
    prefix.append([-1]*10)

    count[i][i-1] = 1
    prefix[i][i-1] = prefix[i-1][9]+1
    for j in range(i,10):
        count[i][j] = count[i][j-1] + count[i-1][j-1]
        prefix[i][j] = count[i][j] + prefix[i][j-1]

ans = -1
row = -1
col = -1
for i in range(1,11):
    for j in range(i-1,10):
        if N <= prefix[i][j]:
            row = i
            col = j
            ans = prefix[i][j]
            break
    if row != -1:
        break

if row == -1:
    ans = -1
    print(ans)
else:
    find([col],1,row, col-1)