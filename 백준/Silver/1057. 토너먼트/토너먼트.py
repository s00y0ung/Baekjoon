N, A, B = map(int, input().split())

m = A if A > B else B #big
n = A if A < B else B #small

t = m-n
t_exp = 0
while 2**t_exp <= t:
    t_exp += 1

if m-n == 1 and m % 2 == 0:
    print(1) # 1ROUND
else:
    for e in range(2,21):

        k = 1
        while k*(2**e) < m:
            k += 1

        if (k-1)*(2**e) < n and m <= k * (2**e):
            print(e)
            break