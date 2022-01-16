upSort = []

for i in range(int(input())):
    num = int(input())
    upSort.append(num)

upSort.sort()
for i in range(len(upSort)):
    print(upSort[i])
