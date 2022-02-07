command = list(input())

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

result = []

for i in range(len(alpha)):
    if alpha[i] in command:
        cnt = command.count(alpha[i])
        result.append(cnt)
    else:
        result.append(0)

for i in result:
    print(i , end=' ')





