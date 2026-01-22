# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 권남훈
# 작성일: 2026. 01. 22. 09:18:16

def solution(s1, s2):
    count = 0
    for i in s1 :
        for j in s2 :
            if i == j :
                count += 1
    return count