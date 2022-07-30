# 20시 35분 (시작) => 21시 (끝)

s = list(map(str,input()))

temp = ""
ans = ""
flag = False

# word를 돌면서 하나씩 값을 비교한다.
for word in s:
    # 모든 조건마다 조건을 걸어서 확인한다.
    if word == "<":
        ans += temp[::-1]
        temp = ""
        temp += word
        flag = True
        continue
    elif word == ">":
        temp += word
        ans += temp[::1]
        temp = ""
        flag = False
        continue

    # flag가 true이면 열린태그이니까 temp에 더해준다.
    if flag:
        temp += word
        continue
    if word == " ":
        ans += temp[::-1] + " "
        temp = ""
        continue
    temp += word

# ans에 마지막 남은거까지 다 역으로 더해서 넣으면 된다.
print(ans + temp[::-1])



