# 17시 10분 (시작) =>
import sys
input = sys.stdin.readline

n = int(input())
board = [list(input()) for _ in range(n)]

def checked(board):
    maxValue = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > maxValue:
                maxValue = cnt
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > maxValue:
                maxValue = cnt
    return maxValue

ans = 0

for i in range(n):
    for j in range(n):
        # 행 바꾸기
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = checked(board)
            if temp > ans:
                ans = temp
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        # 열 바꾸기
        if i+1 < n:
            board[i][j] , board[i+1][j] = board[i+1][j] , board[i][j]
            temp = checked(board)
            # ans = max(temp , ans)
            if temp > ans:
                ans = temp
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(ans)

