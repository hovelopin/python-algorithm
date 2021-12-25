# 1보다 큰 양의 정수 and 1과 자기자신만으로 나누어 떨어지는 ..

N = int(input())

test = list(map(int,input().split()))

cnt = 0 ; sum =0

for i in range(len(test)):
    for j in range(test[i],1,-1):
        if(test[i]%j == 0):
            cnt+=1
    if(cnt==1):
        sum+=1
    cnt = 0
print(sum)


