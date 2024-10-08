CREATE TABLE IF NOT EXISTS marts.gender_trend AS 
SELECT
    tabelldata_kon."Tittarnas kon" AS "Tittarnas kön",
    tabelldata_alder."Tittarnas alder" AS "Tittarnas ålder",
    tabelldata_alder."Genomsnittlig visningslängd"
FROM
    tittare.tabelldata_alder
JOIN
    tittare.tabelldata_kon
ON
    tabelldata_alder."Tittarnas kon" = tabelldata_kon."Tittarnas kon";

-- To view the results:

SELECT
    "Tittarnas kon" AS "Tittarnas kön",
    "Tittarnas alder" AS "Tittarnas ålder",
    "Genomsnittlig visningslängd"
FROM
    marts.gender_trend;



