# 처음에 재귀로 문제를 해결했더니 시간초과 오류가 떴다. => 그래서 그냥 값을 구해놓고 n번째를 추출했음
n = int(input())

resultList = [0,1]

for i in range(45):
    resultList.append(resultList[i]+resultList[i+1])
print(resultList[n])
