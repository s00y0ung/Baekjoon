N = int(input())

d = set()
for i in range(N):
    d.add(input())

d = list(d)
d = sorted(d, key = lambda x : (len(x),x))
for i in d:
    print(i)