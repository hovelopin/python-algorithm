# 1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열!
n,m = map(int,input().split())

sList = []

def f():
    # s의 길이가 m이랑 같다면 리스트를 합쳐서 출력하고 종료
    if len(sList) == m:
        print(' '.join(map(str,sList)))
        return

    # 1부터 n까지 반복문을 돌건데 만일 넣으려는 i가 sList라는 배열에 있으면 다시 조건에 넣는다.
    for i in range(1,n+1):
        if i in sList:
            continue
        # 없으면 넣고 재귀를 넣는다.
        sList.append(i)
        f()
        sList.pop()
f()




