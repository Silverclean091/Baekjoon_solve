N = int(input())
alphaList = [0] * 26

for i in range(N):
    playerName = str(input())
    for j in range (0, 26):
        if playerName[0] == chr(97+j):
            alphaList[j] = alphaList[j] + 1

playerList = []
for i in range (0, 26):
    if alphaList[i] >= 5:
        playerList.append(chr(97+i))

if len(playerList) == 0:
    print("PREDAJA")
else:
    for i in playerList:
	    print(i, end ='')