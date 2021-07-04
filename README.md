# fu_dbs_project_schehrlmar
Ein Projekt dreier Studenten zum Modul Datenbanksysteme an der FU Berlin. Teilnahme im Sommersemester 2021.




Nutzung:
- Starte data_visualisation.html mit den CSV-Dateien 
    gdp_CLEANED-better.csv, 
    population_CLEANED-better.csv, 
    owid-co2-data_CLEANED.csv und 
    world-happiness-index_COMBINED - Kopie2.csv 
  im gleichen Ordner.
- Wähle die zu betrachtenden Länder aus.
- Enjoy!


Eine direkte Verbindung zu einer Datenbank ist leider nicht gelungen. 
Mithilfe des db_client.py Clients kann jedoch via Terminal eine Verbindung zu einer beliebigen Postresql-Datenbank aufgebaut und diese ge-querried, werden.

Entwicklung:
Das Ziel dieser Zweiteiligen Implementierung war es einen einfach zu verwendtbaren Backend Client für SQL-Querries und Entgegennahme der Daten zu nutzen, 
der die erhaltenen Daten  der Datenbank an ein HTML5 Frontend weitergibt. 
Dort würden sie mithilfe Webbassierter Bibliotheken anschaulich und interaktiv dargestellt werden.

Am Ende gelang uns die Verbindung dieser beiden Elemente einfach nicht. 
Alternativen, wie di Node.js Bibliothek "pg" wurden erprobt, aber in dem begrenzten zeitlichen Rahmen war es nicht möglich ein vollständige Lösung zu erarbeiten.

Allerdings konnten die einzelnen Teile fertig gestellt werden. 
Die verwendeten Daten wurden händisch und mithilfe speziefischer Python-Scripte bereinigt und in eine einheitliche Form gebracht.
Eine Datenbank, samt auf passenden Modellen basierendem Schema, konnte zumindest lokal erstellt werden und ist sowohl via vorgefertigten (PG Admin), als auch selbstgeschriebenen Clients erreichbar.

Dieses Repo dokumentiert damit einen noch nicht fertigen, aber fortgeschrittenen Status des Projektes.
