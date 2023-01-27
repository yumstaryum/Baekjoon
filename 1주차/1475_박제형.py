# 방 번호
# https://www.acmicpc.net/problem/1475

N = input() # 방 번호 문자로 받음

set = [0]*10 # 0~9

for i in range(len(N)):
    temp = int(N[i])
    if temp == 9 or temp == 6:
        if set[6] > set[9]:
            temp = 9
        else : temp = 6
    set[temp] += 1

print(max(set))