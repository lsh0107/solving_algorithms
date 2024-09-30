# HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블을 이용해 사원별 성과금 정보를 조회하려합니다. 평가 점수별 등급과 등급에 따른 성과금 정보가 아래와 같을 때, 
# 사번, 성명, 평가 등급, 성과금을 조회하는 SQL문을 작성해주세요.

SELECT      he.EMP_NO,
            he.EMP_NAME,
            CASE
                WHEN hg.s/2 >= 96 THEN 'S'
                WHEN hg.s/2 >= 90 THEN 'A'
                WHEN hg.s/2 >= 80 THEN 'B'
                ELSE 'C'
            END AS GRADE,
            CASE
                WHEN hg.s/2 >= 96 THEN he.SAL * 0.2
                WHEN hg.s/2 >= 90 THEN he.SAL * 0.15
                WHEN hg.s/2 >= 80 THEN he.SAL * 0.1
                ELSE 0
            END AS BONUS
FROM        HR_DEPARTMENT hd
                JOIN HR_EMPLOYEES he
                    ON hd.DEPT_ID = he.DEPT_ID
                JOIN (
                    SELECT      EMP_NO, SUM(SCORE) AS S
                    FROM        HR_GRADE
                    GROUP BY    EMP_NO
                ) hg
                    ON hg.EMP_NO = he.EMP_NO
