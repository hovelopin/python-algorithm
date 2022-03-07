A , P = map(str , input().split())

AList = []

AList.append(A)

while 1:
    result = 0
    for i in AList[-1]:
        result +=int(i)**int(P)
    AList.append(str(result))
    if(AList.count(AList[-1]) > 1):
        idx = AList.index(AList[-1])
        resultList = AList[:idx]
        break
print(len(resultList))



