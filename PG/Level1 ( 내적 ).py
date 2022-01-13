def solution(a, b):
    sumValue = 0
    for i in range(len(a)):
        sumValue += (a[i] * b[i])
    return sumValue

print(solution([1,2,3,4] , [-3,-1,0,2]))