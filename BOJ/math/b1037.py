nCnt = int(input())

nList = list(map(int,input().split()))

nList.sort()

# nList[-1] * 2 한거랑 * 3 한거랑의 결과값의 약수의 갯수를 구해서 nCnt랑 같으면

print(nList[0]*nList[-1])
