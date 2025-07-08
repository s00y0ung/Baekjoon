import heapq

def solution(book_time):
    answer = 0
    for b in range(len(book_time)):
        sbt,sbm = map(int, book_time[b][0].split(':'))
        ebt,ebm = map(int, book_time[b][1].split(':'))
        
        book_time[b] = [sbt*60+sbm, ebt*60+ebm+10]
    book_time = sorted(book_time, key = lambda x : (x[0],x[1]))
    
    hp = []
    heapq.heapify(hp)
    for b in book_time:
        while hp and hp[0] <= b[0]:
            heapq.heappop(hp)
        heapq.heappush(hp,b[1])
        if answer < len(hp):
            answer = len(hp)
        
    return answer