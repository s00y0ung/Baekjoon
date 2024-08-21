testNum = int(input())

for _ in range(testNum):
    floor = int(input())
    room = int(input())
    preList = []
    nList = []

    for i in range(room+1):
        preList.append(i)
        nList.append(i)

    for i in range(floor):
        for j in range(room+1):
            nList[j] = sum(preList[1:j+1])
        preList = nList[:]
        
    
    print(nList[-1])