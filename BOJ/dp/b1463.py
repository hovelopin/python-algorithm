import math

x = int(input())

# 쓰레기값 ( 첫번째 ) , 두번째 , 세번째 , 네번째 , 다섯번째 케이스를 미리 계산해둔다.
dp = [0,0,1,1,2,3]

# x번째까지 최소값을 구해놓은 다음에 dp[x]값을 출력한다.
for i in range(6, x+1):
    # 첫번째 케이스 , 두번째 케이스 , 세번째 케이스의 최소값을 구할꺼임
    one , two , three = math.inf , math.inf , dp[i-1]
    if i % 3 == 0:
        one = dp[i//3]
    if i % 2 == 0:
        two = dp[i//2]

    minValue = min(one, two, three)
    dp.append(minValue + 1)

print(dp[x])
