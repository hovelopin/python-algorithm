# 23시 38분
seatCnt = int(input())
seatInfo = input()

reSeatInfo = seatInfo.replace('LL','*')

resultValue = len(reSeatInfo)
starCnt = reSeatInfo.count('*')

print(resultValue + 1) if starCnt >= 1 else print(resultValue)
