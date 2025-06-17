def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    id_dic = {}
    stop = {}
    for i in id_list:
        id_dic[i] = set()
        stop[i] = 0
        
    for r in report:
        a,b = r.split(' ')
        if b in id_dic[a]:
            continue
        id_dic[a].add(b)
        stop[b] += 1
    
    stop_list = []
    for i in id_list:
        if stop[i] >= k:
            stop_list.append(i)
    
    cnt = 0
    for k in id_list:
        for s in stop_list:
            if s in id_dic[k]:
                answer[cnt] += 1
        cnt += 1
   
    return answer