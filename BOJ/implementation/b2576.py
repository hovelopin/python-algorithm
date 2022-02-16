numList = []
odd = []

for i in range(7):
    numList.append(int(input()))

for j in range(7):
    if(numList[j] % 2 == 1):
        odd.append(numList[j])

if(len(odd) > 0):
    print(sum(odd))
    print(min(odd))
else:
    print(-1)