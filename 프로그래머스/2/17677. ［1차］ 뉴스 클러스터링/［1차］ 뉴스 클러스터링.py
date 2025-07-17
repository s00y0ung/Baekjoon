def solution(str1, str2):
    s1 = []
    s2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    for s in range(len(str1)-1):
        if not str1[s].isalpha() or not str1[s+1].isalpha():
            continue
        s1.append(str1[s]+str1[s+1])
    for s in range(len(str2)-1):
        if not str2[s].isalpha() or not str2[s+1].isalpha():
            continue
        s2.append(str2[s]+str2[s+1])
    
    if len(s1) == 0 and len(s2) == 0:
        answer = 1
    else:
        intersect_list = list(set(s1).intersection(set(s2)))
        tmp = []
        for s in intersect_list:
            m = min(s1.count(s), s2.count(s))
            for i in range(1,m):
                tmp.append(s)
        intersect_list.extend(tmp)
        answer = len(intersect_list) / (len(s1)+len(s2)-len(intersect_list))
        
    return int(answer*65536)