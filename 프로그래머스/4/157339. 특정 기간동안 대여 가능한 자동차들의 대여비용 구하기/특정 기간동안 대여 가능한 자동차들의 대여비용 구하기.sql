-- 세단 or SUV
-- 2022/11/01 ~ 2022/11/30 대여가능
-- 30일간 대여 금액 50만 이상 200만 미만
-- 자동차 ID, 자동차 종류, 대여 금액(FEE)

SELECT      crcc.CAR_ID,
            crcdp.CAR_TYPE,
            ROUND((crcc.DAILY_FEE * 30) * (1 - crcdp.DISCOUNT_RATE * 0.01), 0) AS FEE
FROM        CAR_RENTAL_COMPANY_CAR crcc
            JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY crcrh
                ON crcc.CAR_ID = crcrh.CAR_ID
            JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN crcdp
                ON crcc.CAR_TYPE = crcdp.CAR_TYPE
WHERE       crcc.CAR_TYPE IN ('세단', 'SUV')
            AND crcdp.DURATION_TYPE = '30일 이상'
GROUP BY    crcc.CAR_ID
HAVING      MAX(crcrh.END_DATE) < '2022-11-01'
            AND FEE >= 500000 AND FEE < 2000000
