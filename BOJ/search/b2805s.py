'''
정답은 맞았지만 시간초과 문제!!
1. n과 m의 입력값이 너무 커서 부르트 포스로 구현하면 안될듯
2. 평균값을 이용해서도 풀었는데 시간초과

=> 이분탐색을 이용해서 풀어야 함
'''

import sys

n , m = map(int,sys.stdin.readline().split())

tree = list(map(int,sys.stdin.readline().split()))

# 처음은 0 끝은 tree중에 가장 큰 값을 기준으로 잡는다.
start , end = 0 , max(tree)


while start <= end:
    resultSum = 0
    # 처음과 끝을 2로 나눈 것 => 즉 , 중앙값
    mid = ( start + end ) // 2
    # mid값을 기준으로 큰 나무 높이는 잘림
    for i in tree:
        if(mid < i):
            resultSum += i - mid
    # 원하는 나무 높이보다 더 많이 짤렸으면 start를 올리고 덜 짤렸으면 내려라
    if resultSum >= m :
        start = mid + 1
    else:
        end = mid - 1
print(end)

