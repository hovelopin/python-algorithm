n = int(input())

str = '*'
start = 1

def solution(num):
    global start
    if num == 1:
        return print(str * start)
    print(str * start)
    start += 1

    return solution(num-1);

solution(n)