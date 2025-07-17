def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for p in range(len(phone_book)-1):
        if phone_book[p+1].startswith(phone_book[p]):
            answer = False
            break
    return answer