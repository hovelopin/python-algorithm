# 16시 25분 ( 시작 ) =>  16시 41분 ( 끝 ) =====> 16분
# 왕실의 나이트 ( 구현 )

night= input()
dic = {'a':1 ,'b':2 ,'c':3 ,'d':4 , 'e':5 , 'f':6 ,'g':7 ,'h':8}

night_y = dic[night[0]]
night_x = night[1]


# 전부의 케이스를 dx dy에 담는다.
dx = [2,2,-2,-2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]
cnt = 0

for i in range(8):
    nx = dx[i] + int(night_x)
    ny = dy[i] + int(night_y)
    if (1<= nx < 9 and 1<= ny < 9):
        cnt+=1
print(cnt)

'''
테스트 케이스1
a1
'''
