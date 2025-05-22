N = int(input())
name = [0 for i in range(26)]
for i in range(N):
    s = input().rstrip()
    name[ord(s[0])-97] += 1

f = 0
for i in range(26):
    if name[i] > 4:
        print(chr(i+97), end = '')
        f += 1
if not f:
    print('PREDAJA')