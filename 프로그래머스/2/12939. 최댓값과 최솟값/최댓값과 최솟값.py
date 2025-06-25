def solution(s):
    num_list = [int(x) for x in s.split()]
    answer = str(min(num_list)) +' ' + str(max(num_list))
    return answer