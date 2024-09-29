SELECT      ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME
FROM        ANIMAL_INS ai
        JOIN    ANIMAL_OUTS ao
            ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE       ai.SEX_UPON_INTAKE LIKE 'intact%'
            AND ao.SEX_UPON_OUTCOME NOT LIKE 'intact%'