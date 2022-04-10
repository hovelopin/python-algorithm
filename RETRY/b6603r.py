def lotto(prev , length , newList):
    if length == 6:
        result.append(newList.copy())
        return 0

    for i in range(prev,k):
        newList.append(nList[i])
        lotto(i+1, length+1, newList)
        newList.pop()

while True:
    k , *nList = map(int,input().split())
    result = []

    if k == 0:
        break
    else:
        lotto(0,0,[])
        for i in result:
            print(*i)
        print()

