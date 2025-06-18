def solution(price, money, count):
    answer = -1
    m = 0
    for c in range(1,count+1):
        m += c*price
        
    return max(0, m-money)