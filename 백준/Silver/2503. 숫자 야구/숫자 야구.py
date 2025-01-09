def base_game(abc_list, abc):
    a1,b1,c1 = abc_list[0], abc_list[1], abc_list[2]
    a2,b2,c2 = abc[0], abc[1], abc[2]

    strike, ball = 0,0

    if a1 == a2: strike += 1
    elif a1 in abc : ball += 1

    if b1 == b2: strike += 1
    elif b1 in abc : ball += 1

    if c1 == c2: strike += 1
    elif c1 in abc : ball += 1

    return strike, ball

N = int(input())

abc_list = []
for i in range(123, 988):
    abc = str(i)
    if '0' in abc: 
        continue
    if abc[0] == abc[1] or abc[1] == abc[2] or abc[0] == abc[2]:
        continue        
    abc_list.append(str(i))


for i in range(N):
    abc, strike, ball = map(int, input().split())

    abc_index = 0
    while abc_index < len(abc_list):
        s,b = base_game(abc_list[abc_index], str(abc))
        if strike != s or ball != b: # 생존이 아닌 경우
            del abc_list[abc_index]
            abc_index -= 1
        abc_index += 1

print(len(abc_list))
        
    
    
