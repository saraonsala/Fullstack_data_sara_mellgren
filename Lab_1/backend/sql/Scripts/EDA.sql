WITH 
	date_table AS (SELECT * FROM datum.tabelldata OFFSET 1),
	date_total AS (SELECT * FROM datum.totalt OFFSET 1)
SELECT 
	STRFTIME('%Y-%m-%d', tot.datum), 
	tot.visningar,
	tab.visningar,
	tab."visningstid (timmar)"
FROM date_total as tot
LEFT JOIN date_table as tab 
ON tot.datum = tab.datum;



SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;


--##CREATE SCHEMA IF NOT EXISTS marts;

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



--CREATE TABLE IF NOT EXISTS marts.gender_trend AS 
(
SELECT *
	tittare,
	Tittarnas kön,
	Visningar,
	Visnings
FROM
	tittare.tabelldata_alder);
desc;

SELECT * FROM marts.

desc;




 



