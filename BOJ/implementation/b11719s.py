# EOFError는 더이상 읽어들일 것이 없을 때 발생하는 에러
while 1:
    try:
        print(input())
    except EOFError:
        break
