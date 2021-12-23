# 문제는 맞췄지만 런타임 에러뜨는 코드

N = int(input())

sum = 0

for i in range(N):
    result_seq = []

    cnt = 0

    seq = list(input())
    seq_len = len(seq)

    for j in range(seq_len):
        if (seq_len <= 2):
            cnt += 1
            break
        if(seq[j] == seq[j+1]):
            continue
        else:
            result_seq.append(seq[j])
            if(j+1==seq_len-1):
                result_seq.append(seq[j+1])
                cnt+=1
                break
    for k in range(len(result_seq)):
        if(result_seq.count(result_seq[k])>1):
            cnt=0
    sum+=cnt
print(sum)









