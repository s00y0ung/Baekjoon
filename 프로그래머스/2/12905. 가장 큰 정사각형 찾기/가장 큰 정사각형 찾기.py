def solution(board):

    board_T = [list(x) for x in zip(*board)]
    memory = max(max(board[0]), max(board_T[0]))

    n_row = len(board)
    n_col = len(board[0])


    for col in range(1, n_col):
        for row in range(1, n_row):
            if board[row][col] == 1:
                board[row][col] += min(
                                       board[row-1][col],
                                       board[row][col-1],
                                       board[row-1][col-1]
                                      )
                if memory<board[row][col]:
                    memory = board[row][col]
    return memory**2