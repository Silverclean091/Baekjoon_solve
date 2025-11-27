import sys
input = sys.stdin.readline

# 입력받을 전체 용액의 수 N, 용액의 특성값인 N개의 정수 입력
N = int(input())
koi_list = list(map(int, input().split()))
koi_list.sort()  # 탐색을 위한 정렬

start_koi = 0   # 리스트의 시작값
end_koi = N-1   # 리스트의 끝값
best_koi = sys.maxsize  # 최적의 경우를 탐색하기 위한 초기값(최악의 값)
final_koi = [koi_list[start_koi], koi_list[end_koi]]

while start_koi < end_koi:

    # 현재 진행값 저장 (0에 더 나은 값이 나오면 업데이트)
    currnet_koi = koi_list[start_koi] + koi_list[end_koi]

    # 기존의 최적값과 현재 진행된 값의 절댓값을 비교, 0에 더 가까울 경우 업데이트
    if abs(currnet_koi) < abs(best_koi):
        best_koi = currnet_koi
        final_koi = [koi_list[start_koi], koi_list[end_koi]]

    # 두 용액의 합이 0보다 클 경우, end_koi(음수)의 값 감소
    if currnet_koi > 0:
        end_koi -= 1
    # 두 용액의 합이 0보다 작을 경우, start_koi(양수)의 값 증가
    elif currnet_koi < 0:
        start_koi += 1
    else:  # 두 용액의 합이 0일 경우, 탐색 종료
        final_koi = [koi_list[start_koi], koi_list[end_koi]]
        break

print(final_koi[0], final_koi[1])