N , M = map(int,input().split())

remain_m = 0
remain_n = 0

for i in range(1,min(N,M)+1):
    if(N%i == 0 and M%i == 0):
        gcd = i


remain_m = M // gcd
remain_n = N // gcd

print(gcd)
print(gcd * remain_m * remain_n)
