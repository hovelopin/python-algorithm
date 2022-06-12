# 15시 50분 ( 시작 ) => 16시 4분 ( 끝 )
n = int(input())
hansu = []
cnt = 0

# 1부터 n까지 전부 검사하면서 한수인지 체크해야한다.
for i in range(1,n+1):
    if i <= 99:
        cnt+=1
    # 100이상이라면
    else:
        hundred = i//100
        ten = (i%100)//10
        one = ((i%100)%10)//1
        if hundred-ten == ten-one :
            cnt+=1
print(cnt)

