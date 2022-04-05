import sys

# xList 원소보다 작은것을 구하라
n = int(sys.stdin.readline())
xList = list(map(int,sys.stdin.readline().split()))
newList = sorted(list(set(xList)))

dic = {newList[i] : i for i in range(len(newList))}

for i in xList:
    print(dic[i] , end = ' ')