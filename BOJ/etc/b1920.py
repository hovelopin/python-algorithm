import sys
from collections import Counter


N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

# N을 정렬한다.
# N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int,sys.stdin.readline().split()))

count = Counter(N_list)

for i in M_list:
    if count[i] != 0 :
        print(1)
    else:
        print(0)

