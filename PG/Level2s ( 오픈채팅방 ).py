def solution(record):
    answer = []
    dic = {}

    for sentence in record:
        sentence_split = sentence.split()
        # uid를 key로 name을 value값으로 저장해놓고 enter와 change 일때만 딕셔너리에 넣어준다.
        # 그리고 이름을 바꿔서 들어올때나 안에서 이름을 바꿀때 uid를 기준으로 name값만 바꿔준다.
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if(sentence_split[0] == 'Enter'):
            # 딕셔너리 안에 key값을 넣어서 value값을 추출해준다.
            answer.append(f'{dic[sentence_split[1]]}님이 들어왔습니다.')
        elif(sentence_split[0] == 'Leave'):
            answer.append(f'{dic[sentence_split[1]]}님이 나갔습니다. ')

    print(answer)
    return (answer)

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])