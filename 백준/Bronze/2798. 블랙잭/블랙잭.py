N, M = map(int, input().split())
N_list = list(map(int, input().split()))

blackjack = 0
for i in range(len(N_list)-2):
    for j in range(i+1,len(N_list)-1):
        for k in range(j+1,len(N_list)):
            S = N_list[i] + N_list[j] + N_list[k]
            if S <= M and (M-S)<(M-blackjack):
                blackjack = S
                
print(blackjack)