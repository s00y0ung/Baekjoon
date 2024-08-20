memo = [[1,0], [0,1]]

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if len(memo) < n:
        fibonacci(n-1) + fibonacci(n-2)
        
    if len(memo) == n:
        a = [memo[n-1][0]+memo[n-2][0], memo[n-1][1] + memo[n-2][1]]
        memo.insert(n,a)
    return 0
    
test_count = int(input())
for i in range(test_count):
    b = int(input())
    fibonacci(b)
    print(memo[b][0], memo[b][1])
    memo = [[1,0], [0,1]]
    