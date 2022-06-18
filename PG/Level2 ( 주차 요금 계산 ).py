# 19시 7분 ( 시작 ) =>
def solution(fees, records):
    # fees => 0: 기본 시간 ( 분 ) , 기본 요금 ( 원 ) , 단위 시간 ( 분 ) , 단위 요금 ( 원 )
    dic = dict()
    parking = []
    # 입/출차 내역을 split으로 나눠서 parking 배열에 담는다.
    for i in records:
        parking.append(i.split(" "))
    print(parking)

    # 딕셔너리 안에 번호와 주차 요금을 넣어놓을거임
    for i,j,k in parking:
        dic[j] = 0
    print(dic)

    # parking 배열을 돌아서 시간 , 번호 , in/out 여부를 가지고 반복을돈다. 만일 k가 IN이라면
    for i,j,k in parking:
        if k == 'IN':
            # tiem , number , out 에서 number가 같고 OUT인것을 골라서 돈을 계산한다.
            for time,number,out in parking:
                if j == number and out == 'OUT':
                    print(j , number)
                    time_hour = int(time.split(":")[0]); time_minute = int(time.split(":")[1])
                    i_hour = int(i.split(":")[0]); i_minute = int(i.split(":")[1])
                    acc_time = (time_hour*60 + time_minute) - (i_hour*60 + i_minute)
                    print(acc_time)
                    # parking에서 지우기
                    break
    print(parking)












solution([180, 5000, 10, 600] ,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"] )