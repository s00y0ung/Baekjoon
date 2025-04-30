import sys
input = sys.stdin.readline

def star(N,i,j):
    if N == 3:
        star_list[i][j] = '*'
        star_list[i][j+1] = '*'
        star_list[i][j+2] = '*'
        star_list[i+1][j] = '*'
        star_list[i+1][j+2] = '*'
        star_list[i+2][j] = '*'
        star_list[i+2][j+1] = '*'
        star_list[i+2][j+2] = '*'
        return
    star(N // 3, i+0,j+0)
    star(N // 3, i+0, j+N//3)
    star(N // 3, i+0, j+N//3*2)

    star(N // 3, i+N//3, j+0)
    star(N // 3, i+N//3, j+N//3*2)

    star(N // 3, i+N//3*2,j+0)
    star(N // 3, i+N//3*2, j+N // 3)
    star(N // 3, i+N//3*2, j+N // 3 * 2)

N = int(input())
star_list = [[' ' for _ in range(N)] for _ in range(N)]

star(N,0,0)
for i in range(N):
    print(''.join(star_list[i]))