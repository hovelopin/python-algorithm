# 16시 18분 =>
s = list(input())
flag = False
new = ''
result = ''

for i in s:
    if flag == False:
        if i == '<':
            flag = True
            new += i
        elif i == ' ':
            new += i
            result += new
            new = ''
        else:
            new = i + new
    else:
        new += i
        if i == '>':
            flag = False
            result += new
            new = ""
print(result + new)