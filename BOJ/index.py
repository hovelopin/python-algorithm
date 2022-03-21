# 시작 => 15시 45분
from itertools import combinations

tCase = list(map(int, input().split()))

per = list(combinations(tCase[1:],6))


for i in per:
    for j in i:
        print(j, end =' ')
    print()


