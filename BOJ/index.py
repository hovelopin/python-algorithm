def main():
    print("계산할 수와 연산기호를 입력")
    return input().split(' ')
def cal(c):
    # c = []

    for i in range(0, 1000):
        j = i + 1
        if int(c[1]) == True:
            break
        elif c[j] == '+':
            add(c)
        elif c[j] == '-':
            sub(c)
        elif c[j] == '*':
            mul(c)
        elif c[j] == '/':
            div(c)
        elif c[j] == '//':
            quo(c)
        elif c[j] == '%':
            mod(c)
# 더하기
def add(c):
    return print(int(c[0]) + int(c[i]))
# 빼기
def sub(c):
    return print(int(c[0]) - int(c[i]))
# 곱하기
def mul(c):
    return print(int(c[0]) * int(c[i]))
# 나누기
def div(c):
    return print(int(c[0]) / int(c[i]))
# 몫
def quo(c):
    return print(int(c[0]) // int(c[i]))
# 나머지
def mod(c):
    return print(int(c[0]) % int(c[i]))

while True:
    main = main()
    if cal(main) == False:
        break