testNum = int(input())

# 1 : 1
# 2 : 2, 4, 8, 6
# 3 : 3, 9, 7, 1
# 4 : 4, 6
# 5 : 5
# 6 : 6
# 7 : 7, 9, 3, 1
# 8 : 8, 4, 2, 6
# 9 : 9, 1
# 10 : 10 
power = [[10],[1],[6,2,4,8],[1,3,9,7],[6,4],[5],[6],[1,7,9,3],[6,8,4,2],[1,9]] # lastNum ==> 0번째 자리로
newB = [1,1,4,4,2,1,1,4,4,2]
for i in range(testNum):
    a,b = map(int, input().split())
    last = power[(a%10)][b%(newB[a%10])]
    
    print(last)