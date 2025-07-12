def solution(queue1, queue2):
    indicator2=sum(queue1)-int(sum(queue1+queue2)/2)
    answer=0
    sub_list=(queue1+queue2+queue1)[::-1]
    add_list=(queue2+queue1+queue2)[::-1]
    while indicator2!=0:
        try:
            if indicator2>0:
                indicator2-=sub_list.pop()
            else:
                indicator2+=add_list.pop()
        except:
            return -1
        answer+=1
    return answer
