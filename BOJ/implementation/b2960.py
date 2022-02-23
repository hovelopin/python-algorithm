# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘!
# 정답은 맞았지만 코드가 너무 쓰레기라 ,, 해설을 보자!

resultK = 0

N , K = map(int,input().split())

numberList = []

for i in range(2,N+1):
    numberList.append(i)

while 1:
    j = numberList[0]
    cnt = 0
    P = 0

    for k in range(1, j+1):
        if( cnt > 2 ):
            break
        if( j%k == 0 ):
            cnt+=1
    if cnt == 2 :
        P = j

    for q in numberList:
        if(q%P == 0):
            numberList.remove(q)
            resultK +=1
        if (resultK == K):
            print(q)
            break
    if (resultK == K):
        break


