import sys
input = sys.stdin.readline

# k: 이미 가지고 있는 랜선의 수, n: 필요한 랜선의 수
k, n = map(int, input().split())
lan_cables = [] # 이미 가지고 있는 랜선의 길이 리스트

# 가지고 있는 랜선의 길이 입력
for i in range(k):
    lan_cables.append(int(input()))

max_cable_len = 0  # 자를 수 있는 케이블의 최대 길이
start_num = 1      # 이진 탐색의 시작값
end_num = max(lan_cables)  # 이진 탐색의 끝값(케이블의 최대 길이)

# lan_cables의 중간값으로 요소들을 다 나눈다
# 나눈 몫을 카운트하여 총 카운트된 값이 k값보다 큰지 작은지 본다
# k값보다 작을 경우, 만족하지 못했으므로 중간값을 더 작게 바꾼다.
# k값보다 클 경우, 만족했으므로 최대값을 찾기 위해 중간값을 더 크게 바꾼다.
# 현재의 최대값을 max_cable_len에 저장한다.

# 이진 탐색 시작
while start_num <= end_num:
    mid = (start_num + end_num) // 2
    lan_count = 0  # 잘린 랜선의 개수 카운트
    for i in range(len(lan_cables)):
        lan_count += lan_cables[i] // mid
    if lan_count >= n:
        max_cable_len = mid
        start_num = mid + 1
    else:
        end_num = mid - 1

print(max_cable_len)