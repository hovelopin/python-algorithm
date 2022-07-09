from collections import Counter

def solution(s):
    # res라는 배열을 만들고 s를 반복해서 돌다가 { , }를 제외한 나머지를 넣는다.
    res = []
    for i in s:
        if i == '{' or i == "}":
            continue
        else:
            res.append(i)

    # 그럼 res 배열은 문자들과 ,만 남는다. => 따라서 ,를 기준으로 배열을 만들어주면 숫자 배열들이 만들어진다.
    newRes = "".join(res).split(",")

    # Counter를 이용해서 newRes의 숫자들을 세준다. 그리고 value값을 기준으로 내림차순 정렬을 해준다.
    counter = Counter(newRes)

    counter_sort = sorted(counter.items(), key=lambda x:-x[1])

    ans = []


    for i,j in counter_sort:
        ans.append(int(i))

    return ans

solution("{{20,111},{111}}")