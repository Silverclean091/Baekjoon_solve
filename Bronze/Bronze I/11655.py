S = str(input())
ROT13str = ""

for i in range(len(S)):
    asc = ord(S[i])

    if (asc >= 65 and asc <= 90) or (asc >= 97 and asc <= 122):
        newAsc = asc+13
        if (newAsc > 122):
            ROT13str = ROT13str + chr(newAsc-26)
        elif (asc <= 90) and (newAsc >= 65 and newAsc <= 90):
            ROT13str = ROT13str + chr(newAsc)
        elif (asc <= 90) and (newAsc > 90):
            ROT13str = ROT13str + chr(newAsc-26)
        elif (asc >= 97) and (newAsc <= 122 and newAsc >= 97):
            ROT13str = ROT13str + chr(newAsc)
    else:
        ROT13str = ROT13str + chr(asc)

print(ROT13str)