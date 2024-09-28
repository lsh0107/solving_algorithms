SELECT      ed3.ID
FROM        ECOLI_DATA ed1
        JOIN ECOLI_DATA ed2
            ON ed1.ID = ed2.PARENT_ID
        JOIN ECOLI_DATA ed3
            ON ed2.ID = ed3.PARENT_ID
WHERE       ed1.PARENT_ID IS NULL AND ed2.PARENT_ID IS NOT NULL
ORDER BY    1