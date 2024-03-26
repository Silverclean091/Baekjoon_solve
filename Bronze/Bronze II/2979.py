A, B, C = map(int, input().split())

timeArr = [0] * 100
totalPrice = 0

for i in range(3):
    arriveTime, leaveTime = map(int, input().split())
    for j in range(arriveTime, leaveTime):
        timeArr[j] += 1

for i in timeArr:
    if i == 1:
        totalPrice = totalPrice + A
    elif i == 2:
        totalPrice = totalPrice + 2*B
    elif i == 3:
        totalPrice = totalPrice + 3*C

print(totalPrice) 