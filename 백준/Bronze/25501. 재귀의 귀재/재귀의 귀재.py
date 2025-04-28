n = int(input())
for _ in range(n):
    s = input()

    recur = 1
    isP = 1
    for idx in range(len(s)//2):
        if s[idx] != s[len(s)-idx-1]:
            isP = 0
            break
        recur += 1
    print(isP, recur)