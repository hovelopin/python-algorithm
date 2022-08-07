# 19시 45분 ( 시작 ) => 19시 48분 ( 끝 )

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))
