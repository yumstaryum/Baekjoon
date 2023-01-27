# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n = int(input())
result = 0

for i in range(n):
    alphabet = [0]*26
    word = input()
    for j in range(0, len(word)):
        if j>0 and word[j] == word[j-1]:
            continue
        alphabet[ord(word[j])-97] += 1 # a : 97, ord : char -> int 

    group = True
    
    for k in alphabet:
        if k>=2:
            group = False
            break
        else:
            pass

    if group == True:
        result += 1

print(result)