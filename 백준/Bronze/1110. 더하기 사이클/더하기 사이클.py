N = int(input())

cycle = 1
ten = N // 10
one = N % 10
s = one*10 + (ten+one)%10

while s != N:
    ten = s // 10
    one = s % 10
    s = one*10 + (ten+one)%10
    cycle += 1

print(cycle)