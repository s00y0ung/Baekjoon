import functools

def comparator(a, b):
    t1 = a+b
    t2 = b+a
    
    return (int(t1)-int(t2))
    
def solution(numbers):
    n = list(map(str, numbers))
    n = sorted(n, key = functools.cmp_to_key(comparator), reverse = True)
    answer = str(int(''.join(n)))
    return answer