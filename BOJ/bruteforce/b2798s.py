# 순열을 이용하면 더욱 쉽게 해결할수있다.
from itertools import permutations

n,m = map(int,input().split())

num = list(map(int,input().split()))
permutationArray = permutations(num,3)

newArray = []

for i in permutationArray:
    if(m>=sum(i)):
        newArray.append(sum(i))
print(max(newArray))

