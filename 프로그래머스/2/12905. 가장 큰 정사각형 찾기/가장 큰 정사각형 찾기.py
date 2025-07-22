def solution(board):
    answer = 0

    dp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            if board[i-1][j-1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                if answer < dp[i][j]:
                    answer = dp[i][j]
    return answer **2