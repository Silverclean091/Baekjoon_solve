T = int(input())

for i in range(T):
    numberList = list(map(int, input().split()))
    numberList.sort()
    print(numberList[-3])