def solution(a, b):
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    dayofweek = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    day = -1
    for i in range(1,a):
        day += month[i]
    day += b

    return dayofweek[day%7]