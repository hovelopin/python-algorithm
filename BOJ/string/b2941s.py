# replace를 사용하는 어렵지 않은 문제!
alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

language = input()

cnt = 0

for i in alphabet:
    language = language.replace(i,'*')
print(len(language))
