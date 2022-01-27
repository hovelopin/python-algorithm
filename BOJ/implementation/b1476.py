# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
E , S , M = map(int,input().split())

cnt = 0

earth = 1 ; sun = 1 ; moon = 1

while 1 :
    cnt += 1
    if (earth > 15):
        earth -= 15
    if (sun > 28):
        sun -= 28
    if (moon > 19):
        moon -= 19
    if(earth == E and sun == S and moon == M ):
        break
    earth+=1 ; sun+=1 ;moon+=1

print(cnt)