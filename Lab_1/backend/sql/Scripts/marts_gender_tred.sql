CREATE TABLE IF NOT EXISTS marts.gender_trend AS 
SELECT
    tabelldata_kon."Tittarnas alder" AS "Tittarnas ålder",
    tabelldata_alder."Tittarnas kon" AS "Tittarnas kön",
FROM
    tittare.tabelldata_alder
INNER JOIN
    tittare.tabelldata_kon
ON
    tittare.tabelldata_alder."Tittarnas kon" = tittare.tabelldata_kon."Tittarnas alder" 


