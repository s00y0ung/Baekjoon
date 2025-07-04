def solution(people, limit):
    answer = 0
    people.sort()
    si, ei = 0, len(people)-1
    
    while si <= ei:
        if people[si] + people[ei] <= limit:
            si += 1
            ei -= 1
        else:
            ei -= 1
        answer += 1
            
    return answer