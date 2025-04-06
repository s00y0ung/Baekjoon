def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x

A, B = map(int, input().split())
C, D = map(int, input().split())

lcm = B * D // gcd(B, D)
tmp = (A * (lcm // B)) + (C * (lcm // D))
t = gcd(tmp, lcm)
print(tmp//t, lcm//t)