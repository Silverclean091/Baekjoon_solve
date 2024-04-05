s = str(input())
s = s.upper()

alphaList = [0]*26

for i in range (len(s)):
    alphaList[ord(s[i])-65] += 1

max_value = max(alphaList)
max_index = []

for i in range (len(alphaList)):
    if alphaList[i] == max_value:
        max_index.append(alphaList.index(max_value))

if len(max_index) > 1:
    print("?")
else:
    print(chr(max_index[0]+65))