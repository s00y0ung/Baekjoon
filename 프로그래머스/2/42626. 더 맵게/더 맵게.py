import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        s1 = scoville[0]
        heapq.heappop(scoville)
        s2 = scoville[0]
        heapq.heappop(scoville)
        
        heapq.heappush(scoville,s1+s2*2)
        answer += 1
        
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    return answer