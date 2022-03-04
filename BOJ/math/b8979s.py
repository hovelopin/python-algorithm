import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [list(map(int,input().split())) for _ in range(n)]

# 정렬할때 람다 형식을 이용한다.
# 키값을 람다 x로 두고 x[1] 하면 2차원 배열에 1번 열을 통해 정렬한다 => -붙인 이유는 내림차순으로 해야하기 때문에
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))

print(s)

# k번째 순번을 찾아서 index에 넣어둔다.
for i in range(n):
    if s[i][0] == k:
        index = i
print(index)

# 인덱스번째의 값이랑 내가 찾는 값이 같으면 거기 등수에 +1하면 된다.
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break