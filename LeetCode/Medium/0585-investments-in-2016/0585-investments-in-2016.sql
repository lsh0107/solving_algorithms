SELECT      ROUND(SUM(TIV_2016), 2) AS TIV_2016
FROM        INSURANCE
WHERE       TIV_2015 IN (
            SELECT      TIV_2015
            FROM        INSURANCE
            GROUP BY    TIV_2015
            HAVING      COUNT(TIV_2015) > 1
            )
            AND CONCAT(LAT, ', ', LON) NOT IN (
            SELECT      CONCAT(LAT, ', ', LON)
            FROM        INSURANCE
            GROUP BY    LAT, LON
            HAVING      COUNT(CONCAT(LAT, ', ', LON)) > 1
            )

