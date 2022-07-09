combi = [('1','2','3'), ('4','5','6')]
nums = '123'
cnt1 = 0
cnt2 = 0
for i,j,k in combi:
    list(nums)
    if i == nums[0]:
        cnt1+=1
    if j == nums[1]:
        cnt1+=1
    if k == nums[2]:
        cnt1+=1
    if nums.count(i) != 0:
        cnt2 += 1
    if nums.count(j) != 0:
        cnt2 += 1
    if nums.count(k) != 0:
        cnt2 += 1

    print(cnt1 , cnt2)

