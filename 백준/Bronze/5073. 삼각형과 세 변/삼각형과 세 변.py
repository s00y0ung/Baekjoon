f,s,t = map(int, input().split())
while(f != 0):
    leng = [f,s,t]
    leng.sort()
    if leng[2] >= leng[0]+leng[1]:
        print("Invalid")
    elif f == s == t:
        print("Equilateral")
    elif f == s or s == t or f == t:
        print("Isosceles")
    else:
        print("Scalene")

    f,s,t = map(int, input().split())