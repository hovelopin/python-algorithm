# 17시 36분 시작 => 40분끝 ( 4분걸림 )

N = int(input())

# A,B 리스트를 입력받는다.
A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = 0

# 규칙을 보니까 A의 최소값이랑 B의 최댓값을 곱해주면 그게 S의 최솟값이다.
for i in range(N):
    aMin = min(A)
    bMax = max(B)
    A.remove(aMin)
    B.remove(bMax)
    S += aMin * bMax
print(S)