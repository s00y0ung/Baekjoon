def solution(people, limit):
    answer = 0
    people.sort()
    si, ei = 0, len(people)-1
    
    while si <= ei:
        s = people[ei]
        ei -= 1
        if s + people[ei] <= limit:
            s += people[ei]
            ei -= 1
            answer += 1
            continue

        if s + people[si] <= limit:
            s += people[si]
            si += 1
        answer += 1
            
    return answer