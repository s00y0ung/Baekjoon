import sys

n = int(input())
li = list(map(int, sys.stdin.read().split()))

li.sort()

for x in li:
    sys.stdout.write(str(x) + '\n')