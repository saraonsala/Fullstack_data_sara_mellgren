CREATE TABLE IF NOT EXISTS marts.gender_trend_clean_data AS (
WITH 
	Tittare.tabelldata_kon AS (SELECT * FROM tittare.tabelldata_kon."Tittarnas alder"),
	tittare.tabelldata_alder ta AS (SELECT * FROM  tittare.tabelldata_alder."Tittarnas kon")
SELECT 
	tittare.tabelldata_alder."Tittarnas kon" ,
	tittare.tabelldata_kon."Tittarnas alder" 
	tittare.tabelldata_kon."Genomsnittlig visningslängd" 
FROM tittare.tabelldata_alder ta as "Kön"
LEFT JOIN tittare.tabelldata_kon e as "ålder" 
ON tittare.tabelldata_alder = tittare.tabelldata_kon;






---CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.videos_title AS 
(
SELECT
	STRFTIME('%Y-%m-%d',
	Datum) AS Datum ,
	Videotitel,
	Visningar
FROM
	innehall.diagramdata);


SELECT * FROM marts.videos_title;
CREATE TABLE IF NOT EXISTS marts.gender_trend_clean_data AS (
SELECT
	tittare.tabelldata_kon "Tittarnas alder" AS "Tittarnas ålder",
	tittare.tabelldata_alder."Tittarnas kon" AS "Tittarnas kön",
FROM
	tittare.tabelldata_alder
INNER JOIN
    tittare.tabelldata_kon
ON
	tittare.tabelldata_alder."Tittarnas kon" = tittare.tabelldata_kon."Tittarnas alder";

	sum(Visningar) AS Visningar
FROM
	enhetstyp.diagramdata d
GROUP BY
	(datum,
	Enhetstyp )
ORDER BY 
	"Tittarens_kön" );

CREATE TABLE IF NOT EXISTS marts.device_summary AS (
SELECT
	Enhetstyp,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	"Genomsnittlig visningslängd" AS Visningslängd_genomsnitt
FROM
	enhetstyp.tabelldata );


CREATE TABLE IF NOT EXISTS marts.gender_trend AS (
SELECT
	tittare.tabelldata_kon "Tittarnas alder" AS "Tittarnas ålder",
	tittare.tabelldata_alder."Tittarnas kon" AS "Tittarnas kön",
FROM
	tittare.tabelldata_alder
INNER JOIN
    tittare.tabelldata_kon
ON
	tittare.tabelldata_alder."Tittarnas kon" = tittare.tabelldata_kon."Tittarnas alder";







-- checks
SELECT * FROM marts.device_views_date;
SELECT * FROM marts.device_summary;