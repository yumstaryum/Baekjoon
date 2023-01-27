# 사탕 게임
# https://www.acmicpc.net/problem/3085
# 브루트포스 이용

N = int(input())
board =[list(input()) for _ in range(N)] # board color 입력
max_cnt = 0

def check(): # 현재 board 상황에서 max_cnt()
    global max_cnt
    for i in range(N):
        cnt = 1 
        # 행 검사
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
        cnt = 1
        # 열 검사
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1

for i in range(N):
    for j in range(N):
        # 오른쪽과 바꿈
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 아래와 바꿈
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_cnt)