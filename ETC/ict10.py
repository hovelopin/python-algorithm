# 23시 8분 ( 시작 ) =>  23시 20분 ( 끝 ) =====>  12분
# 곱하기 혹은 더하기 ( 그리디 )
s = list(map(int,input()))

sumResult = s[0]

for i in range(1,len(s)):
    if(sumResult==0 or s[i] == 0 or s[i] == 1):
        sumResult += s[i]
    else:
        sumResult *= s[i]

print(sumResult)


"""
테스트케이스 1 
02984

테스트케이스 2 
567
"""
