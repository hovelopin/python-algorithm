from collections import deque

# tc의 개수
tc = int(input())

for i in range(tc):
    N,M = map(int,input().split())
    # N개가 입력되고
    nFile = deque(map(int,input().split()))
    cnt = 0
    while nFile:
        # nFile에서 가장 큰 값을 top으로 정한다.
        top = max(nFile)
        M-=1
        first = nFile.popleft()
        if( top != first ):
            nFile.append(first)
            # top이랑 first가 같지 않고 M=-1이라는 것은 M은 맨뒤로 갔다는 소리
            if(M < 0):
                M = len(nFile) - 1
        else:
            cnt +=1
            if M == -1:
                print(cnt)
                break






