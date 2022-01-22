'''
딕셔너리에 중복되는 값을 넣을때 값이 하나만 들어가는 오류 발생!

딕셔너리로는 접근을 못하는건가??? 다시 고민해보기

=> cnt값을 추가해 중복되는 값들을 차이를 둔다.

'''

import sys

result = []
cnt = 0

for i in range(int(sys.stdin.readline())):
    age , name = map(str,sys.stdin.readline().split())
    cnt += 1
    user = {'name':name , 'age': age , 'cnt' : cnt}
    result.append(user)

# lambda식을 이용해서 정렬을 해주었다.
ageSort = sorted(result , key= lambda x : (x['age'] , x['cnt']))

# f-string으로 정렬할때는 안됐다,,
for dic in ageSort:
     print(dic['age'] + ' ' + dic['name'])

