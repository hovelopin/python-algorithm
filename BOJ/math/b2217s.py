# 해설까지 1시간정도

'''
문제를 이해하지 못했었음 10과 15가 있을때 두 로프가 각각 버틸수있는 무게는 최소무게를 기준으로 잡는다.
그래서 10이된다.
15를 기준으로 잡으면 10은 사용할 수 없기 때문에 15*1 => 15가 최대
10을 기준으로 잡으면 10 , 15 둘다 사용할 수 있기 때문에 10*2 =>20이 최대!
풀이를 rope의 역순으로 정렬한 후에 값을 하나씩 늘려가면서 최대 용량을 확인한다!!

'''
import sys

N = int(sys.stdin.readline())

rope = []
result = []
cnt = 1

for i in range(N):
    rope.append(int(sys.stdin.readline()))
rope.sort(reverse=True)

for j in range(N):
    value = rope[j]*cnt
    result.append(value)
    cnt+=1
print(max(result))
