# Code-Referenz der X4-Scripts

Dieser Überblick fasst wichtige Funktionen und Aufrufe der vorhandenen Skripte zusammen. Besonderes Augenmerk liegt auf Befehlen, die Informationen über die Spielwelt und den Spieler liefern.

## Verwendete Bibliotheksfunktionen

| Funktion | Datei | Beschreibung |
| --- | --- | --- |
| `lib.find.sectors.inrange` | `08/aiscripts/lib.find.sectors.inrange.xml` | Sucht Sektoren in einer bestimmten Gate-Distanz zu einem Referenzobjekt und berücksichtigt Blacklists. |
| `lib.find.point.indeepspace` | `08/aiscripts/lib.find.point.indeepspace.xml` | Ermittelt einen sicheren Punkt im tiefen Raum eines Sektors unter Berücksichtigung von Stationsabständen. |
| `order.restock.subordinates` | `08/aiscripts/order.restock.subordinates.xml` | Nutzt `find_cluster_in_range`, um benachbarte Cluster zu sammeln und Schiffe nach Besitzer zu suchen. |
| `interrupt.disengage` | `08/aiscripts/interrupt.disengage.xml` | Beispiel für die Prüfung, ob ein Objekt spielereigen ist, und das Handling von indestructible Targets. |
| `fight.attack.object.fighter` | `08/aiscripts/fight.attack.object.fighter.xml` | Zeigt die Verwendung von `find_ship`, um Versorger in einem Sektor zu finden. |
| `order.move.die` | `08/aiscripts/order.move.die.xml` | Greift auf `player.age` und `player.entity.hascontext` zu, um die Präsenz des Spielers zu prüfen. |

## Befehle zur Informationssammlung

Diese Befehle treten in den Skripten häufig auf, wenn Daten über die Spielwelt oder den Spieler benötigt werden:

- `<find_sector>` / `<find_sector_in_range>` – liefert Sektoren für ein Objekt oder innerhalb einer Reichweite.
- `<find_cluster_in_range>` – listet Cluster in einer bestimmten Gate-Distanz.
- `<find_station>` – sucht Stationen in einem Sektor, optional nach Besitzern gefiltert.
- `<find_ship>` / `<find_ship_by_true_owner>` – findet Schiffe nach Klasse, Besitzer oder Job.
- `<find_object>` – allgemeine Suche nach Objekten.
- `<find_gravidar>` – durchsucht Gravidar-Kontakte innerhalb einer Region.
- `<find_buy>` / `<find_sell>` – Handelsabfragen für Warenpreise in der Umgebung.
- `<get_safe_pos>` – berechnet eine sichere Position in einem Sektor basierend auf Mindest- und Maximalabstand.
- `distanceto` / `gatedistance` – Funktionen zur Distanzberechnung zwischen Objekten oder Sektoren.
- `isplayerowned` – Boolean-Eigenschaft zur Prüfung, ob ein Objekt dem Spieler gehört.
- `player.entity` und `player.entity.hascontext` – Zugriff auf das Spielerobjekt; nützlich, um zu prüfen, ob der Spieler sich auf einem Schiff befindet oder ein Kontext aktiv ist.
- `player.age` – Alter der aktuellen Spielsitzung, oft für Zeitvergleiche verwendet.

Diese Referenz dient als Einstieg für das Verständnis der Skripte und liefert eine Auswahl häufig verwendeter Befehle zur Informationsgewinnung über Spielwelt und Spieler.
