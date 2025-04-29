def cantor(n):
    if n == 1:
        return '-'
    left = cantor(n//3)
    center = ' '*(n//3)
    return left+center+left

while True:
    try:
        N = int(input())
        print(cantor(3**N))
    except EOFError:
        break