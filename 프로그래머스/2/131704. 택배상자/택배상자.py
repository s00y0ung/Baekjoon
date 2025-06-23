def solution(order):
    answer = []
    box = [0 for _ in range(len(order))] 
    for i, v in enumerate(order):
        box[v-1] = i+1
    
    stack = []
    box = box[::-1]
    for i in range(1, len(order)+1):
        if stack and stack[-1] == i:
            answer.append(i)
            stack.pop()
            continue
        
        while box and box[-1] != i:
            stack.append(box[-1])
            box.pop()
            
        if not box:
            break
        answer.append(box[-1])
        box.pop()
        
    return len(answer)