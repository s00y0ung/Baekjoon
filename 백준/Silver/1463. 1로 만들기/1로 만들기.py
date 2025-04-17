def solve(x):
    if x in ans:
        return ans[x]
    return 1 + min(solve(x//3)+x%3, solve(x//2) + x%2)

N = int(input())
ans = {1:0, 2:1, 3:1}

print(solve(N))