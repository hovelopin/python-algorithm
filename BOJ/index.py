# 연습장

def solution(solve):
  start = solve[0]
  cnt = 0

  for i in range(1,len(solve)):
    # 값을 비교해서 반전이 일어나면 짤라서 확인한다.
    if (start < solve[i]):
      start = solve[i]
      cnt +=1
    else:
      # 값을 자를때 자르는 값 이후의 값들을 비교해서 어디까지 반전이 일어나지 않나 확인한다.
      for j in range(cnt,len(solve)-1):
        if(solve[j] > solve[j+1]):
          cnt+=1
      # 짜른 값을 solve에 넣는다.
      solve = solve[0:cnt+1]
      break
  print(start)
  print(solve)
  return solve

solution([0, 1, 2, 5, 3, 7])

'''
계산 방법 
if (짜른 배열 == 3 ):
  1개가 나오고 
# 3개보다 큰 것들 
else:
  1. start를 기준으로 양쪽의 갯수가 같으면 그 양쪽의 갯수를 각각 더하는거고 
  2. start를 기준으로 양쪽의 갯수가 같지 않아 그리고 start가 왼쪽에 가까우면 오른쪽의 갯수 오른쪽에 가까우면 왼쪽의 갯수 
  3. 구한 갯수를 result값에 넣어서 return 하면 될 듯? 
'''