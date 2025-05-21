def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

nums = list(map(int, input().split()))
answer = 1000000

for i in range(3):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            answer = min(answer, lcm(lcm(nums[i], nums[j]), nums[k]))
print(answer)