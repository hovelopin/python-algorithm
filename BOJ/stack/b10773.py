import sys

money = []
k = 0

for i in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())

    if(len(money) == 0 ):
        money.append(n)
        continue
    else:
        money.append(n)
        k+=1
        if(money[k] == 0):
            money.pop(k)
            money.pop(k - 1)
            if(len(money) == 0):
                k=0
            else:
                k = len(money)-1

print(sum(money))
