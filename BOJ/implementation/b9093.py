# 15시 32분 => 15시 41분 ==> 9분
t = int(input())

for j in range(t):
    tcList = list(input().split())
    result = ''
    for i in tcList:
        result += f"{i[::-1]} "
    print(result)
