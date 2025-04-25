a = int(input())
dna1 = [0] + list(input().rstrip())
b = int(input())
dna2 = [0] + list(input().rstrip())

d = [[0 for _ in range(a+1)] for _ in range(b+1)]

for i in range(1, b+1):
    for j in range(1, a+1):
        if dna2[i] == dna1[j]:
            d[i][j] = max(3,d[i-1][j-1] + 3)
        else:
            d[i][j] = max(d[i-1][j-1]-2,d[i-1][j]-2, d[i][j-1]-2, 0)

#최대 값 찾기
er = 0
ec = 0
val = -1000000
for i in range(1, b+1):
    v = max(d[i][1:])
    if v > val:
        er = i
        ec = d[i].index(v)
        val = v
print(val)

i,j = er,ec
li1 = []
li2 = []
while d[i][j] != 0:
    if dna1[j] == dna2[i]:
        li1.append(dna1[j])
        li2.append(dna2[i])
        i -= 1
        j -= 1
    else:
        if d[i-1][j] >= d[i][j-1]:
            li2.append(dna2[i])
            i -= 1
        else:
            li1.append(dna1[j])
            j -= 1

print(''.join(li1[::-1]))
print(''.join(li2[::-1]))