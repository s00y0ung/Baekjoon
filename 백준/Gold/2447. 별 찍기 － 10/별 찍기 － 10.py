def star(n) :
    if n == 3 :
        return  ["***","* *","***"]
    div = n//3
    res = []
    l = star(div)
    for i in l :
        res.append(i*3)
    for i in l :
        res.append(i+' '*(div)+i)
    for i in l :
        res.append(i*3)
    return res

N = int(input())
print("\n".join(star(N)))