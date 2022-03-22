# 18시 =>

# 수빈 채널 = 100
# 이동 채널 = n

n = int(input())
m = int(input())

if m!=0:
    arr = list(map(int,input().split()))
else:
    arr = []

subinCh = 100
ans = abs(n-subinCh)

for i in range(1000001):
    numArr = list(str(i))
    flag = False
    # 숫자를 누를 수 있는지 검사
    # arr안에 담긴 애들은 부러진 놈들이라 i가 arr안에 있으면 안됨!
    for k in numArr:
        if int(k) in arr:
            flag =True
            break
    # false면
    if flag:
        continue
    # 숫자를 누를 수 있다면 n까지 가는 방법 + 숫자를 누른 횟수를 구해서 비교한다.
    else:
        ans = min(ans , abs(n-i) + len(str(i)))

print(ans)
