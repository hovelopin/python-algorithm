'''
정답은 맞았지만 시간초과 문제!!
1. n과 m의 입력값이 너무 커서 부르트 포스로 구현하면 안될듯
2. 평균값을 이용해서도 풀었는데 시간초과

=> 이분탐색을 이용해서 풀어야 함
'''

import sys

n , m = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

# 트리의 중간값을 설정해놓고 기준으로 삼는다.
maxHeight = int(sum(tree)/len(tree))

while 1:
    resultSum = 0
    for i in tree:
        if(maxHeight < i):
            result = i - maxHeight
            resultSum += result
    if(resultSum == m):
        print(maxHeight)
        break
    maxHeight += 1


