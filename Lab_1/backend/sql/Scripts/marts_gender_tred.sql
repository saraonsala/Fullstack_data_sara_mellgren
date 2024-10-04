CREATE TABLE IF NOT EXISTS marts.gender_trend AS 
SELECT*
FROM
	tittare.tabelldata_alder
JOIN tittare.tabelldata_kon
ON
	tabelldata_alder."Tittarnas kon" = tabelldata_kon. "Tittarnas alder";
