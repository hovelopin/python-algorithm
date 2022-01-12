def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]

    for i in numbers:
        for j in num:
            if(numbers.count(j) == 1):
                num.remove(j)
    sumValue = sum(num)
    return sumValue


print(solution([1,2,3,4,6,7,8,0]))