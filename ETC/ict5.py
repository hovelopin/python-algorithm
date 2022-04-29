# 15시 38분 ( 시작 ) =>  15시 56분 ( 끝 ) =====> 18분
# 시각 ( 구현 )
n = int(input())
cnt = 0
# 00시 00분 00초부터 n시 59분 59초까지 3이 하나라도 포함

for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                cnt+=1
print(cnt)

'''
테스트 케이스1
5
'''
