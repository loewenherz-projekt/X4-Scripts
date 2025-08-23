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

Die Skripte nutzen diverse Abfragen, um Informationen über Spielwelt oder Spieler zu erhalten:

- `<find_dockingbay>` – ermittelt verfügbare Andockplätze an einem Objekt, z.B. bei der Erzeugung von Trägerschiffen【F:extensions/ego_dlc_split/ext_03/md/setup_gamestarts.xml†L249-L251】
- `<find_gate>` – sucht Tore oder Beschleuniger innerhalb eines Sektors【F:extensions/ego_dlc_split/ext_03/md/story_split.xml†L367-L368】
- `<find_cluster>` – sammelt Cluster nach Makrokennung, z.B. für Terraforming-Prozesse【F:extensions/ego_dlc_split/ext_03/md/terraforming.xml†L16-L18】
- `<find_zone>` – identifiziert Zonen in einem Sektor und kann nach Highways filtern【F:08/aiscripts/order.fight.patrol.xml†L139-L143】
- `<find_sector>` / `<find_sector_in_range>` – liefert Sektoren für ein Objekt oder innerhalb einer Reichweite【F:extensions/ego_dlc_split/ext_03/md/story_paranid.xml†L16-L17】
- `<find_station>` / `<find_station_by_true_owner>` – sucht Stationen im Raum und filtert nach Besitzer oder Funktion【F:extensions/ego_dlc_split/ext_03/md/x4ep1_war_subscriptions.xml†L209-L211】
- `<find_ship_by_true_owner>` – listet Schiffe eines Besitzers in einem Sektor oder der gesamten Galaxie auf【F:extensions/ego_dlc_split/ext_03/md/story_split.xml†L330-L332】
- `player.entity` und `player.entity.hascontext` – Zugriff auf das Spielerobjekt, um zu prüfen, ob der Spieler sich auf einem Schiff befindet oder ein Kontext aktiv ist【F:08/aiscripts/order.move.die.xml†L41-L45】
- `player.age` – Alter der aktuellen Spielsitzung, häufig für Zeitvergleiche genutzt【F:08/aiscripts/order.move.die.xml†L41-L41】

Diese Referenz dient als Einstieg für das Verständnis der Skripte und liefert eine Auswahl häufig verwendeter Befehle zur Informationsgewinnung über Spielwelt und Spieler.

## Zusätzliche Befehle aus dem DeadAir Scripts Repository

| Funktion | Datei | Beschreibung |
| --- | --- | --- |
| `find_sector` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Sammelt alle Sektoren für die dynamische Nachrichten-Queue【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L76-L87】 |
| `find_station` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Filtert wichtige Stationstypen wie Werften oder Handelsstationen【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L77-L86】 |
| `find_station_by_true_owner` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Ermittelt Stationen eines bestimmten Besitzers, z.B. für Xenon-Entwicklungsstufen【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L114-L120】 |
| `find_ship_by_true_owner` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Sucht Schiffe eines Besitzers rekursiv in der gesamten Galaxie【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L842-L848】 |
| `find_cluster` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Durchläuft alle Cluster im Universum und prüft Exklusivitätsregeln【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L6886-L6903】 |
| `player.money` | `/tmp/deadair_scripts/md/deadairdynamicuniversemenus.xml` | Vergleicht das Spielerguthaben mit Kosten für Menüoptionen【F:/tmp/deadair_scripts/md/deadairdynamicuniversemenus.xml†L1222-L1226】 |
| `player.age` | `/tmp/deadair_scripts/md/deadairdynamicuniverse.xml` | Zeitstempel für Ereignisse und Prüfungen in der dynamischen Kriegsführung【F:/tmp/deadair_scripts/md/deadairdynamicuniverse.xml†L289-L352】 |
