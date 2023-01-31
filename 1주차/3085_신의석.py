# 사탕 게임
# https://www.acmicpc.net/problem/3085
def eatMax(cList):# 최대로 먹을 수 있는 값을 출력하는 함수
    Max = 1
    for i in range(num):
        countrow = 1
        for j in range(num-1):
            if cList[i][j] == cList[i][j+1]:
                countrow+=1
                Max = max(Max,countrow)
            else:
                countrow = 1
    for j in range(num):
        countcol = 1
        for i in range(num-1):
            if cList[i][j] == cList[i+1][j]:
                countcol += 1
                Max = max(Max,countcol)
            else:
                countcol = 1
    return Max

num = int(input())
cList =[]

for i in range(num):# C,P,Z,Y가 들어오면 이차원 배열의 형태로 리스트 생성
    k=input()
    k = k.replace('C', ' C ')
    k = k.replace('P', ' P ')
    k = k.replace('Z', ' Z ')
    k = k.replace('Y', ' Y ')
    k = k.split()
    cList.append(k)

result = 0
for i in range(num):#행끼리 교환하면서 최대개수 result에 초기화
    for j in range(num-1):
        cList[i][j], cList[i][j+1]= cList[i][j+1],cList[i][j]
        temp = eatMax(cList)#eatMax에서 나온 값을 temp에 저장 후
        if temp>result:#result와 비교 후 result값 초기화
            result = temp
        cList[i][j], cList[i][j+1]= cList[i][j+1],cList[i][j]

for j in range(num):#열끼리 교환하면서 최대개수 result에 초기화
    for i in range(num-1):
        cList[i][j], cList[i+1][j] = cList[i+1][j], cList[i][j]
        temp = eatMax(cList)#eatMax에서 나온 값을 temp에 저장 후
        if temp>result:#result와 비교 후 result값 초기화
            result = temp
        cList[i][j], cList[i+1][j] = cList[i+1][j], cList[i][j]
print(result)