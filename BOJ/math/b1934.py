# 최대공약수를 이용하여 간단하게 계산하였다.
from math import gcd

T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    # 최대공약수를 large라고 한다.
    large = gcd(a,b)
    # a,b를 각각 large로 나눴을때의 몫을 구한다.
    a //= large
    b //= large
    # 최대공약수 * a몫 * b몫 => result 결과
    result = large * a * b
    print(result)



