# Stellenanzeigen-Crawler für service.bund.de

## Überblick
Dieses Projekt beinhaltet einen Web-Crawler, der speziell für das Extrahieren von Stellenangeboten von der Website [service.bund.de](https://www.service.bund.de) entwickelt wurde. Die Daten werden für eine wissenschaftliche Arbeit an der HTW Dresden gesammelt und ausgewertet.

## Funktionen
- Durchsucht service.bund.de nach offenen Stellen.
- Extrahiert Titel und Beschreibung der Stellenanzeige.
- Speichert die gesammelten Daten im json-Format.

## Anforderungen
- Python 3
- Bibliotheken: `requests`, `beautifulsoup4`, `json`