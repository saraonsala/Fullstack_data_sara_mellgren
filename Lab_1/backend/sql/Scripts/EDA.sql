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








