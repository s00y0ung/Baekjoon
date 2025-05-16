def solution(friends, gifts):

    size = len(friends)
    gift_table = [[0 for _ in range(size)] for _ in range(size)]
    p_num = {v:i for i, v in enumerate(friends)}  # 친구 num
    g_rate = [0 for _ in range(size)]  # 선물 지수
    answer = [0 for _ in range(size)]
    for g in gifts:
        giver, receiver = g.split()

        g_rate[p_num[giver]] += 1
        g_rate[p_num[receiver]] -= 1
        gift_table[p_num[giver]][p_num[receiver]] += 1

    for i in range(size):
        for j in range(size):
            if i == j:
                continue

            if gift_table[i][j] > gift_table[j][i]:
                answer[i] += 1
            elif gift_table[i][j] == gift_table[j][i]:
                if g_rate[i] > g_rate[j]:
                    answer[i] += 1

    return max(answer)