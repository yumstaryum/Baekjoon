# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
num = int(input())

count=0
for i in range(num):
    w = input()
    wBool =1
    for j in range(len(w)-1):
        if w[j]==w[j+1]:
            wBool=1
        elif w[j] in w[j+1:]:
            wBool=0
            break
    if wBool:
        count +=1

print(count)