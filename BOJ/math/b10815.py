from collections import Counter
import sys

# 17시10분 => 17시 17분

n = int(sys.stdin.readline())
nList = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))

nList = Counter(nList)

for i in mList:
    if nList[i] >= 1:
        print(1 , end =' ')
    else:
        print(0 , end= ' ')

