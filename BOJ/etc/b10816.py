from collections import Counter

N =int(input())
card = list(map(int,input().split()))

# counter 모듈을 사용하였다.
# counter는 딕셔너리형태로 값을 출력해주고 key값의 개수를 세서 value에 넣어준다.
cnt = Counter(card)

M = int(input())
cntCard = list(map(int,input().split()))

# conter로 들어가 있는 곳에 접근해서 값을 추출해준다.
for i in cntCard :
    print(cnt[i] , end=' ')


