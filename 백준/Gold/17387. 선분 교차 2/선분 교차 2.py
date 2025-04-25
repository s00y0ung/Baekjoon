x1,y1,x2,y2 = map(int, input().split())
x3,y3,x4,y4 = map(int, input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)

c1 = ccw(x1,y1,x2,y2,x3,y3)
c2 = ccw(x1,y1,x2,y2,x4,y4)
c3 = ccw(x3,y3,x4,y4,x1,y1)
c4 = ccw(x3,y3,x4,y4,x2,y2)

if c1*c2 <= 0 and c3*c4 <= 0:
    if c1*c2 == 0 and c3*c4 == 0:
        a1,a2,a3,a4 = x1,x2,x3,x4
        if a1 == a2:
            a1,a2,a3,a4 = y1,y2,y3,y4
        if max(a1,a2) >= min(a3,a4) and max(a3,a4) >= min(a1,a2):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
