# 재귀 함수를 이용하여 10진수를 2진수로 변환하시오

def convertBinary(n):

    if n < 2:
        print(n,end ='')
    else:
        convertBinary(n//2)
        print(n%2,end = '')

n = int(input())
print(convertBinary(n))