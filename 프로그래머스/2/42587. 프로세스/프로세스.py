def solution(priorities, location):
    answer = 0
    que = [i for i in range(len(priorities))]
    cnt = 0
    while priorities:
        m = max(priorities)
        for i in range(len(priorities)):
            if priorities[0] != m:
                priorities.append(priorities[0])
                que.append(que[0])
                priorities.pop(0)
                que.pop(0)
            else:
                if que[0] == location:
                    cnt = 1
                priorities.pop(0)
                que.pop(0)
                answer += 1
                break

        if cnt:
            break

    return answer