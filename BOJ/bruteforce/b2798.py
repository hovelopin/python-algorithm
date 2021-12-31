N , M = map(int,input().split())

score = list(map(int,input().split()))

# 정렬
score.sort()

sum = 0

new_score = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=score[i]+score[j]+score[k]
            if(sum<=M):
                new_score.append(sum)
                continue
print(max(new_score))




