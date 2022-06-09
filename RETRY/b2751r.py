# 19시 52분 시작 => 19시 55분 끝 ( 3분 )
import sys
n = int(sys.stdin.readline())
nList = []

for i in range(n):
    nList.append(int(sys.stdin.readline()))
sortNList = sorted(nList)

for i in sortNList:
    print(i)