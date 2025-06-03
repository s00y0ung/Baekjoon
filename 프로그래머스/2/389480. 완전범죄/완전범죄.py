def solution(info, n, m):
    global min_sum # A가 훔친 최솟값
    min_sum = 10000
    visited=[] # 방문여부
    def dfs(r, idx, a_sum, b_sum):
        global min_sum
        visited.append([r,a_sum,b_sum]) 
        if r == len(info)-1: # 마지막 도달
            if min(min_sum, a_sum) == a_sum and a_sum < n and b_sum <m:
                min_sum = a_sum
            return
        if a_sum >= n or b_sum >= m or min_sum < a_sum: # A도둑의 합이 최소가 되어야함 => 최소보다 크면 return
            return
        if [r+1,a_sum+info[r+1][0],b_sum] not in visited: # 방문 안했을때만 탐색
            dfs(r+1,0,a_sum+info[r+1][0],b_sum) # 0번 선택 
        if [r+1,a_sum,b_sum+info[r+1][1]] not in visited: # 방문 안했을때만 탐색
            dfs(r+1,1,a_sum,b_sum+info[r+1][1]) # 1번 선택 
            
            
    dfs(0,0,info[0][0],0) # A도둑시작
    dfs(0,1,0,info[0][1]) # B도둑시작
    if min_sum == 10000: # 붙잡히면 -1 리턴 
        return -1
    return min_sum