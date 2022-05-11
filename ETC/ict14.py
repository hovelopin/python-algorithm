# 20시 8분 ( 시작 ) => 20시 14분 ( 끝 )
# 럭키 스트레이트 ( 구현 )
n = list(map(int,input()))
if(sum(n[:len(n)//2]) == sum(n[len(n)//2:])):
    print(f'LUCKY')
else:
    print(f'READY')

"""
테스트케이스 1 
123402

테스트케이스 2 
7755
"""
