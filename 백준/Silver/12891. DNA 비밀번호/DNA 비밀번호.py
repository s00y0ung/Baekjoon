s, p = map(int, input().split())
dna = input()
a,c,g,t = map(int, input().split())

dna_dic = {'A':0, 'C':0, 'G':0, 'T':0}
ans = 0

for i in range(p):
    dna_dic[dna[i]] += 1
if dna_dic['A'] >= a and dna_dic['C'] >= c and dna_dic['G'] >= g and dna_dic['T'] >= t:
    ans += 1

for i in range(p, s):
    dna_dic[dna[i-p]] -= 1
    dna_dic[dna[i]] += 1
    if dna_dic['A'] >= a and dna_dic['C'] >= c and dna_dic['G'] >= g and dna_dic['T'] >= t:
        ans += 1
print(ans)