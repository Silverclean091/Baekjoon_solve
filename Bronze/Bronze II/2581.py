M = int(input())
N = int(input())

primeNumberList = []

for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            primeNumberList.append(i)

if len(primeNumberList) > 0:
    print(sum(primeNumberList))
    print(min(primeNumberList))
else:
    print('-1')