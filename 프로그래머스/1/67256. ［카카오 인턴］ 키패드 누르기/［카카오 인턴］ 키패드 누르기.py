def solution(numbers, hand):
    answer = ''
    left = [0,0]
    right = [0,0]
    num = {0:[1,0],1:[0,3],2:[1,3],3:[2,3],4:[0,2],5:[1,2],6:[2,2]
          ,7:[0,1],8:[1,1],9:[2,1]}
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = num[n]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = num[n]
        else:
            l_move = [abs(a-b) for a,b in zip(num[n], left)]
            r_move = [abs(a-b) for a,b in zip(num[n], right)]
            if sum(l_move) > sum(r_move):
                answer += 'R'
                right = num[n]
            elif sum(l_move) < sum(r_move):
                answer += 'L'
                left = num[n]
            else:
                if hand == "right":
                    answer += 'R'
                    right = num[n]
                else:
                    answer += 'L'
                    left = num[n]
                
            
    
    return answer