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


CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.content_new AS 
(
SELECT 
	STRFTIME('%Y-%m-%d'), 
    d.Datum AS Diagram_Datum,
    d.Innehall AS Diagram_Innehall,
    d.Videotitel AS Diagram_Videotitel,
    d.Publiceringstid_för_video AS Diagram_Publiceringstid,
    d.Visningar AS Diagram_Visningar,
    t.Videotitel AS Tabelldata_Videotitel,
    t.Visningar AS Tabelldata_Visningar,
    t.Visningstid_timmar,
    t.Prenumeranter,
    t.Exponeringar,
    t.Klickfrekvens_för_exponeringar,
    tot.Datum AS Totalt_Datum,
    tot.Visningar AS Totalt_Visningar
FROM 
    Innehåll_Diagramdata d
INNER JOIN 
    Innehåll_Tabelldata t
ON 
    d.Innehåll = t.Innehåll 
    AND d.Videotitel = t.Videotitel
LEFT JOIN 
    Innehåll_Totalt tot
ON 
    d.Datum = tot.Datum);
   
-- ## Beskrivning
   
CREATE SCHEMA IF NOT EXISTS marts;
CREATE TABLE IF NOT EXISTS marts.content_tittare AS 
(     
SELECT 
    a.Tittare, 
    a.Tabelldata_kon, 
    b.Tabelldata_alder
FROM 
    tittardata a
INNER JOIN 
    tittardata b
ON 
    a.Tittare = b.Tittare
WHERE 
    a.Tabelldata_kon IS NOT NULL
AND 
    b.Tabelldata_alder IS NOT NULL);


  
   
desc;




 



