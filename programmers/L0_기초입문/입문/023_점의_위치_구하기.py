# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 권남훈
# 작성일: 2026. 01. 22. 09:10:12

def solution(dot):
    if dot[0] > 0 and dot[1] > 0 :
        return 1
    elif dot[0] < 0 and dot[1] > 0 :
        return 2
    elif dot[0] < 0 and dot[1] < 0 :
        return 3
    elif dot[0] > 0 and dot[1] < 0 :
        return 4