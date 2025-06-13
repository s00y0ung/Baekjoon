def solution(ingredient):
    answer = 0
    burger = []
    
    for b in ingredient:
        burger.append(b)
        if burger[-4:] == [1,2,3,1]:
            for i in range(4):
                burger.pop()
            answer += 1
            
    return answer