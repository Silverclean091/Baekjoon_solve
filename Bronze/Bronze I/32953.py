import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())   # 수업의 수, 교수의 기준
students = []  # 학번들을 저장할 리스트 선언

# 수업의 수만큼 반복
# 학생의 수 입력, 학생의 수만큼 학번 입력, 리스트에 저장
for i in range(N):
    K = int(input())
    student = list(input().split())
    students.extend(student)

cnt = Counter(students)  # 리스트에 있는 학번들의 등장 횟수 카운트
student_num = 0  # 정답이 될 학생 수

# 교수의 기준인 M번 이상 학번이 등장하는 학생의 수 카운트
for i in cnt.values():
    if i >= M:
        student_num += 1

print(student_num)