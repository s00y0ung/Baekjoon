def is_palindrome(s,l,r):
    global recur
    recur += 1

    if l >= r:
        return 1
    if s[l] != s[r]:
        return 0
    return is_palindrome(s, l+1, r-1)

n = int(input())
for _ in range(n):
    s = input()

    recur = 0
    print(is_palindrome(s, 0, len(s)-1), recur)