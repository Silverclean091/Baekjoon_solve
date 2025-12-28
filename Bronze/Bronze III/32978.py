import sys
input = sys.stdin.readline

N = int(input())   # 요리 재료의 개수 N 입력
ingredient = set(input().split())   # 요리에 필요한 재료 집합
hyeonbin_ing = set(input().split()) # 현빈이가 사용한 재료 집합

for x in ingredient - hyeonbin_ing:  # 두 재료의 차집합
    print(x)