import sys

N = int(sys.stdin.readline())

sum = 1
cnt = 0

for i in range(1,N+1):
    sum*=i

a = list(str(sum))

for j in range(len(a)-1,0,-1):
    if(a[j] == '0'):
        cnt+=1
    else:
        break

print(cnt)

