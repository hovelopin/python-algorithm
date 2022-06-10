import sys
n = int(sys.stdin.readline())
meeting = []
cnt_meeting = 0

for i in range(n):
    x , y = map(int,sys.stdin.readline().split())
    meeting.append([x,y])

# 끝나는 시간 별로 오름차순 정렬을 진행하고 시작한 순서대로 오름차순으로 정렬을 진행한 상태에서 cnt_meeting 값을 구한다.
meeting.sort(key=lambda x:(x[1] , x[0]))

standard = meeting[0][1]
for i in range(1, n):
    if(standard <= meeting[i][0]):
        standard = meeting[i][1]
        cnt_meeting += 1
print(cnt_meeting + 1)

