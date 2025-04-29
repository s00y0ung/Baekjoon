import sys
input = sys.stdin.readline

N = int(input())
que = []
front = -1
rear = -1
for _ in range(N):
    n_list = input().split()
    if n_list[0] == 'push':
        que.append(int(n_list[1]))
        rear += 1

    elif n_list[0] == 'pop':
        if front == rear:
            print(-1)
        else:
            print(que[front+1])
            front += 1

    elif n_list[0] == 'size':
        print(rear - front)

    elif n_list[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)

    elif n_list[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(que[front+1])

    elif n_list[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(que[rear])