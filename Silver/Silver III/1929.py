M, N = map(int, input().split())
primeList = [True] * (N+1)
primeList[0] = False
primeList[1] = False

for i in range(2, int(N**0.5)+1):
    if primeList[i] == True:
        for j in range(2*i, N+1, i):
            primeList[j] = False

for i in range(M, N+1):
    if i > 1 and primeList[i] == True:
        print(i)