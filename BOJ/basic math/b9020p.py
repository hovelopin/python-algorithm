# 에라토스의 채부터 다시 공부하고 다시 풀자!

sosu_list = []


def sosu(i):
    cnt = 0

    for j in range(2,int(i**0.5)+1):
        if(i == 1):
            sosu_list.append(1)
        if(i%j == 0):
            cnt+=1
    else:
        sosu_list.append(j)
sosu(1)
print(sosu_list)





