computer = int(input())

virus = set()

for i in range(int(input())):
    x,y = map(int,input().split())
    # 초기 x,y에 집어넣고
    if x not in virus:
        virus.add(x)
        if y not in virus:
            virus.add(y)

print(virus)