def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = str(format(arr1[i]|arr2[i],'b')).rjust(n,'0')
        answer.append(''.join(['#' if i ==  '1'else ' ' for i in s]))
        
    return answer
