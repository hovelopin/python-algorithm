'''
처음에 input으로 입력받아서 시간초과 나왔던 문제!!
문제 조건 보고 시간복잡도 확인 잘 하자!!
문제는 어렵지 않았음
'''

import sys

list = []

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    list.append(num)

# sort()와 sorted()는 시간복잡도가 nlogn 이다.
resultList = sorted(list)

# 리스트에 있는 값을 한줄씩 호출할때는 반복문보다 join을 이용해서 호출하자!!
for i in resultList:
    print(i)
