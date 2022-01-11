def solution(number, k):
    answer = []

    # num배열에 숫자들을 넣고
    for num in number:
        # not 배열 => 배열이 비어있으면
        if not answer:
            answer.append(num)
            continue

        if k > 0:
            # while문을 통해서 마지막값이 push할 값보다 작으면 마지막 값을 빼버린다
            while answer[-1] < num:
                answer.pop()
                k -= 1
                # 배열이 비어있거나 k가 0보다 작거나 같을때는 반복문 종료!!
                if not answer or k <= 0:
                    break
        # 종료후에 append
        answer.append(num)
    # 최종 값 출력..
    return ''.join(answer)


solution('4177252841', 4)