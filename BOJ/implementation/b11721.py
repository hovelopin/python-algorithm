command = input()

start = 0
end = 10

# 10씩 끊어서 사용하기 때문에 10으로 나눈 몫 + 1
numbers = len(command) // 10

# 10씩 늘린다. 0:10 => 10:20 => 20:30 ...
for i in range(numbers + 1):
    print(command[start:end])
    start+=10
    end+=10
