# 방 번호
# https://www.acmicpc.net/problem/1475
num = input()
numList = []
for i in range(0,10):
    numList.append(num.count(str(i)))

special = (numList[6]+numList[9])//2 + (numList[6]+numList[9])%2
numList[6] = special
numList.pop()
print(max(numList))