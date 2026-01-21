# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 권남훈
# 작성일: 2026. 01. 21. 11:06:17

def solution(array, height):
    count = 0
    for i in array :
        if i > height :
            count += 1
    return count