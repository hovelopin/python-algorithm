from itertools import permutations

n = int(input())
a = list(map(int,input().split()))

cases = list(permutations(a))

answer = 0
for case in cases:
    check = 0
    for i in range(n-1):
        check += abs(case[i] - case[i+1])
    answer = max(answer,check)
print(answer)