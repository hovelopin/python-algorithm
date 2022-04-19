# 두 문자열 A,B가 주어질 때 , A의 모든 알파벳이 문자열 B에 존재하는지 판별하는 프로그램을 작성하세요.  (재귀)

cnt = 0

def strContain(A,B):
    global cnt
    if len(A) == cnt:
        return print('Yes')
    else:
        if A[cnt] not in B:
            print('No')
            exit()
        cnt += 1
        strContain(A,B)

A = input()
B = input()
strContain(A,B)