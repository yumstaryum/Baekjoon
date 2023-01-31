# 에라스토테네스의 체
# https://www.acmicpc.net/problem/2960
Num, K= map(int, input().split())
numList = []
for i in range(2,Num+1):
    numList.append(i)
order = 0
while True:
    if order>=K:
        break
    temp = min(numList)
    unit = min(numList)
    i = temp - 2
    while temp <= Num:
        if numList[i] == temp:
            order += 1
            if order == K:
                print(numList[i])
                break
            numList[i] = 1001
        i += unit
        temp += unit