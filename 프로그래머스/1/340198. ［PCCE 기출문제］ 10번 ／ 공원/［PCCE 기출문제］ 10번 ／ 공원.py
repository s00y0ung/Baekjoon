def access(mat, park, st_row, st_col):
    for r in range(st_row, st_row+mat):
        for c in range(st_col, st_col+mat):
            if r < len(park) and c < len(park[0]):
                if park[r][c] != "-1":
                    return False
            else:
                return False
    return True
    
def solution(mats, park):
    row = len(park)
    col = len(park[0])
    mats.sort(reverse = True)
    
    for m in mats:
        for r in range(row):
            for c in range(col):
                if access(m,park,r,c):
                    return m

    return -1
