# 20시 45분 (시작) => 21시 5분 (끝)
from itertools import combinations_with_replacement

n = int(input())

dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
words = ['I', 'V', 'X', 'L']
ans = set()

cb = list(combinations_with_replacement(words, n))

for i in cb:
    sumValue = 0
    for word in i:
        sumValue += dic[word]
    ans.add(sumValue)

print(len(ans))