x , y = map(int,input().split())

# 1,3,5,7,8,10,12 => 31일
# 4,6,9,11 => 30일
# 2월 => 28일

'''
월요일을 기준으로 쭉 나열해보니까 x월을 기준으로 그 앞에 월의 날짜를 다 더해서 date를 만들어주고 y-1만큼 숫자들 더한것의 7로 나눈 나머지가
0인것을 월요일이라고 기준으로 잡고 해결! 
'''

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT' , 'SUN']

month = [31,28,31,30,31,30,31,31,30,31,30,31]

date = 0

for i in range(x-1):
    date += month[i]
date += y-1

if(date % 7 == 0):
    print(day[0])
elif(date % 7 == 1):
    print(day[1])
elif(date % 7 == 2):
    print(day[2])
elif(date % 7 == 3):
    print(day[3])
elif(date % 7 == 4):
    print(day[4])
elif(date % 7 == 5):
    print(day[5])
elif(date % 7 == 6):
    print(day[6])



