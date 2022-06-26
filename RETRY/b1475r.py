# 18시 35분 ( 시작 ) => 18시 55분 ( 끝 )
from collections import defaultdict
"""
0~9까지의 숫자 세트를 파는데 6=>9 , 9 => 6 으로 바꿀 수 있음
"""
n = map(str,input())
res = 0
maxValue = 0

room = defaultdict(int)

for i in n:
    if i =='6' or i== '9':
        room['6'] += 1
    else:
        room[i] += 1

for k,v in room.items():
    if k =='6':
        if v%2 == 0:
            maxValue = v//2
        else:
            maxValue = v//2 + 1
    else:
        maxValue = v
    res = max(maxValue, res)
print(res)
