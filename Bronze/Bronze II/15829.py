import sys
input = sys.stdin.readline

L = int(input())  # 문자열의 길이 L
text = input()    # 해시함수로 변환할 문자열 text

r = 31
M = 1234567891
hash_value = 0  # 결괏값을 저장할 변수

for i in range(L):
    tmp = ord(text[i]) - 96  # 아스키코드 - 96 : a부터 1, 2, 3, ...
    hash_value = (hash_value + tmp * (r**i)) % M 
    # 문제에서 제시한 예시대로 계산하되, 식에 맞게 Mod 1234567891을 해주어야 함
    # % M 연산이 들어가지 않을 경우 정답이 50점으로 인정

print(hash_value)