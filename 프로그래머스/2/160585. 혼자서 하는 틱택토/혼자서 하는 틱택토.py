def solution(board):
    fn,xn = 0, 0
    for i in range(3):
        fn += board[i].count('O')
        xn += board[i].count('X')
        
    if fn - xn != 0 and fn - xn != 1:
        return 0
    
    fc = 0
    xc = 0
    for i in range(3):
        if board[i] == 'OOO':
            fc += 1
        if board[i] == 'XXX':
            xc += 1
    
    for i in range(3):
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            fc += 1
        elif board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            xc += 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O': fc += 1
        if board[0][0] == 'X': xc += 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O': fc += 1
        if board[0][2] == 'X': xc += 1
            
    if fn == xn:
        if fc == 0:
            return 1
    if fn > xn:
        if xc == 0:
            return 1
    return 0