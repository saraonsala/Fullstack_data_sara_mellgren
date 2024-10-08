CREATE TABLE IF NOT EXISTS marts.gender_trend AS 
SELECT
    tabelldata_kon."Tittarnas kon" AS "Tittarnas kön",
    tabelldata_alder."Tittarnas alder" AS "Tittarnas ålder",
    tabelldata_alder."Genomsnittlig visningslangd" AS "Genomsnittlig visningslängd",
FROM
    tittare.tabelldata_alder
INNER JOIN
    tittare.tabelldata_kon
ON
    tabelldata_alder."Tittarnas kön" = tabelldata_kon."Tittarnas ålder";



