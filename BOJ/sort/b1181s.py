# sort를 사용할때 길이 먼저 정렬하고 그냥 정렬했더니 값이 안나옴..
# 하지만 그냥 정렬하고 길이를 정렬하면 길이순 - 알파벳순으로 잘 정렬됨..

words = []

for i in range(int(input())):
    command = input()
    words.append(command)

'''
set(list)같은 명령은 단순히 list를 set으로 바꿔줄 뿐이지, 그 타입을 그대로 list라는 변수에 저장해주지 않는다.
그렇기 때문에 set_lst라는 변수를 선언해서 그 값을 따로 저장해주고, 그 값을 list로 다시 변환해준다.
'''

# 중복을 제거 한 후 다시 list에 넣는다.
words_set = set(words)
words = list(words_set)

# 알파벳정렬 후 길이 정렬
words.sort()
words.sort(key=len)

for i in words:
    print(i)