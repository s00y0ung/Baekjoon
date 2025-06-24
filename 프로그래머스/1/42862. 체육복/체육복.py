def solution(n, lost, reserve):
    _lost = [l for l in lost if l not in reserve]
    _reserve = [r for r in reserve if r not in lost]   
    _lost.sort()
    
    for l in _lost:
        if l-1 in _reserve:
            _reserve.remove(l-1)
        elif l+1 in _reserve:
            _reserve.remove(l+1)
        else:
            n -= 1
    
    return n