n, k = map(int, input().split())
cnt = 0
'''
배열의 크기를 이렇게 잡는 이유를 모르겠었는데 
인덱스대로 접근하려면 idx가 n+1개여야만 한다. 
ex) n = 7이라 2~7까지 확인해야한다. 이때 편하게 하기 위해 우리는 0부터 7까지 만들고 0,1은 버리고 2에서 7까지만 사용한다. 
'''

nums = [True] * (n + 1)

# 2부터 N까지 ..
for i in range(2, n + 1):
    # i의 배수만큼 움직여야하기 때문에
    for j in range(i, n + 1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break