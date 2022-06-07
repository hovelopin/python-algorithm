# 22시 55분 ( 시작 ) => 22시 ( 끝 )
# 위에서 아래로 ( 정렬 )

n = int(input())

answer = []

for i in range(n):
    answer.append(int(input()))

answer.sort(reverse=True)
for i in answer:
    print(i , end =' ')


"""
테스트 케이스 1)
3
15
27
12
"""