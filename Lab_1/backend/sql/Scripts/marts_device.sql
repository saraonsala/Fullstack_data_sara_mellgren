CREATE TABLE IF NOT EXISTS marts.device_views_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	datum) AS Datum,
	Enhetstyp,
	sum(Visningar) AS Visningar
FROM
	enhetstyp.diagramdata d
GROUP BY
	(datum,
	Enhetstyp )
ORDER BY 
	Datum ASC );

CREATE TABLE IF NOT EXISTS marts.device_summary AS (
SELECT
	Enhetstyp,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	"Genomsnittlig visningslängd" AS Visningslängd_genomsnitt
FROM
	enhetstyp.tabelldata );



-- checks
SELECT * FROM marts.device_views_date;
SELECT * FROM marts.device_summary;

SELECT Enhetstyp, count(*) total_rows, sum(Visningar) as total_visningar 
from 
enhetstyp.diagramdata group by Enhetstyp ;

select * from enhetstyp.diagramdata d ;

SELECT * EXCLUDE (Innehåll) FROM  innehall.tabelldata ORDER BY "Visningstid (timmar)" DESC OFFSET 1 LIMIT 5;

SELECT * FROM  innehall.diagramdata;-- ORDER BY "Visningstid (timmar)";

SELECT STRFTIME('%Y-%m-%d', Datum), Visningar FROM innehall.totalt;