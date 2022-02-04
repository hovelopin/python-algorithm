star = int(input())

cnt = star

for i in range(star):
    command = '*' * cnt
    print(command)
    cnt -= 1
