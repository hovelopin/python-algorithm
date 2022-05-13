# 22시 8분 ( 시작 ) => 22시 15분 ( 끝 )
# 문자열 재정렬 ( 구현 )
s = list(input())

num = []
seq = []

for i in s:
    if i.isalpha() == True:
        seq.append(i)
    else:
        num.append(int(i))
# 문자들을 오름차순으로 정렬하고 num의 합을 변수에 저장한다.
seqSort = sorted(seq)
numSum = sum(num)

print(f'{"".join(seqSort)}{numSum}')

"""
테스트케이스 1 
K1KA5CB7

테스트케이스 2 
AJKDLSI412K4JSJ9D
"""
