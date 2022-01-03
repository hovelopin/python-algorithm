N = int(input())

rank =[]
score = []

for i in range(N):
    w,h = map(int,input().split())
    score.append((w,h))

for j in score:
    cnt = 1
    for k in score:
        if(j[0] < k[0] and j[1] < k[1]):
            cnt+=1
    rank.append(cnt)
print(score)
print(rank)

for j in score:
    print(j)
    for k in score:
        print(k)

