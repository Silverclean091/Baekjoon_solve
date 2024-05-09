N = int(input())
score = input()
studentLst = list(map(int, score.split()))

studentLst.sort()
answer = studentLst[-1] - studentLst[0]
print(answer)