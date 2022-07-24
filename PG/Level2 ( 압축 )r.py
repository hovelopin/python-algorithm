from string import ascii_uppercase

def solution(msg):
    res = []
    dict = {}
    alphabetCnt = 0
    # 파이썬의 알파벳 모듈을 활용하여 dict를 채운다.
    for i in ascii_uppercase:
        alphabetCnt += 1
        dict[i] = alphabetCnt

    # 27부터 시작하기 위해서 1을 증가시킨다.
    for i in range(len(msg)-1):
        alphabetCnt += 1
        temp = ""
        while True:
            # 키로 값을 조회해서 value값이 있는지 확인하고 있으면 temp에 잠시 넣어둔다.
            temp += msg[i]
            print(temp)
            value = dict.get(temp)
            # value값이 있으면 true라 통과 없으면 none이라 통과못함
            if value:
                i += 1
                # res.append(dict[temp])
            else:
                dict[temp] = alphabetCnt
                break
    print(res)
    print(dict)

solution("KAKAO")