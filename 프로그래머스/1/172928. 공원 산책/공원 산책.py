def solution(park, routes):
    answer = []
    direction = {'S': (1, 0), 'N': (-1, 0), "W": (0, -1), 'E': (0,1)}

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                answer.append(i)
                answer.append(j)
                break
    
    for r in routes:
        dx, dy = direction[r[0]]
        step = int(r[2])
        for s in range(1,step+1):
            if 0 > answer[0]+s*dx or answer[0]+s*dx >= len(park):
                step = 0
                break
            if 0 > answer[1]+s*dy or answer[1]+s*dy >= len(park[1]):
                step = 0
                break
            if park[answer[0]+s*dx][answer[1]+s*dy] == 'X':
                step = 0
                break
        answer[0] = answer[0] + step*dx
        answer[1] = answer[1] + step*dy


    return answer