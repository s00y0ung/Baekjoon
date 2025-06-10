def solution(s, skip, index):
    answer = []
    alpha = {}
    sk_alpha = [chr(i) for i in range(97,123)]
    for sk in skip:
        sk_alpha.remove(sk)

    for i in range(26):
        if chr(i+97) in skip:
            continue
        alpha[chr(i+97)] = sk_alpha[(sk_alpha.index(chr(i+97)) + index) % len(sk_alpha)]
    for ch in s:
        answer.append(alpha[ch])
    return ''.join(answer)