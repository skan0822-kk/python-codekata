# 식품분류별 가장 비싼 식품의 정보 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131116
# 작성자: 권남훈
# 작성일: 2026. 01. 19. 09:28:41

-- 코드를 입력하세요
SELECT
    category,
    price as max_price,
    product_name
from (
    SELECT
        CATEGORY,
        PRICE,
        PRODUCT_NAME,
        ROW_NUMBER() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) AS RN
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
) as T
where RN=1
ORDER BY PRICE DESC