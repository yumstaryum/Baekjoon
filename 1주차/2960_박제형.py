# 에라스토테네스의 체
# https://www.acmicpc.net/problem/2960

N, K = map(int, input().split()) 

num = [0]*(N+1)
cnt = 0

for i in range(2, N+1):
    if num[i]==0:
        for j in range(i, N+1, i): # i부터 N까지 i만큼 증가하면서 
            if num[j] == 0: # 0이면
                num[j] = 1 # 1로 바꿔줌
                cnt += 1 # cnt++
                if cnt == K: 
                    print(j)