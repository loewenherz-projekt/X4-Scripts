# Befehle und Funktionen zur Informationsabfrage

Diese Übersicht fasst nützliche Befehle und Funktionen zusammen, um Daten über Spielwelt und Spieler zu erhalten. Die Angaben basieren auf `CODE_REFERENCE.md`, `SCRIPT_COMMAND_REFERENCE.md` und `LUA_FUNCTION_REFERENCE.md`.

## Schiffe
- `<find_ship>` – sucht Schiffe nach Name, Raum oder Makro.
- `<find_ship_by_true_owner>` – listet Schiffe eines Besitzers mit Filtern für Klasse, Zweck oder Fraktion.
- `<get_ship_definition>` – liefert Informationen zu einem Schiffsmakro für eine bestimmte Fraktion.
- `<get_ship_build_wares>` – gibt benötigte Waren zum Bau eines Schiffs zurück.
- `Helper.addShipComparison` – erstellt einen UI-Vergleich zwischen Schiffen.

## Fraktionen
- `<get_factions_by_relation>` – gibt Fraktionen nach ihrer Beziehung zu einer Referenzfraktion zurück.
- `<get_factions_by_tag>` – listet Fraktionen mit einem bestimmten Tag.

## Handelsdaten
- `<get_highest_resource_yield>` – ermittelt die höchste Ressourcenausbeute in einem Sektor für eine Ware.
- `<get_resource_gatherrate>` – liefert Sammelraten einer Ressource.
- `<get_ware_definition>` – holt Informationen zu einem Warenmakro.
- `<get_ware_reservation>` – zeigt reservierte Waren eines Objekts.
- `<get_wares_illegal_to>` – listet illegale Waren für eine Fraktion auf.

## Spielerdaten
- `player.entity` und `player.entity.hascontext` – Zugriff auf das Spielerobjekt bzw. Prüfung auf aktuellen Kontext.
- `player.age` – Alter der aktuellen Spielsitzung.
- `GetLiveData` – liefert Live-Daten eines Components (z.B. für UI-Elemente).
- `GetTargetMonitorDetails` – gibt detaillierte Informationen zu einem Zielmonitor zurück.

## Sektoren
- `<find_sector>` – sucht Sektoren nach Name oder Makro.
- `<find_sector_in_range>` – findet Sektoren innerhalb einer bestimmten Gate-Distanz zu einem Objekt.
- `<get_satellite_coverage>` – ermittelt die Satellitenabdeckung eines Sektors.
- `<get_zone_at_position>` – liefert die Zone an einer bestimmten Position.

## Flotten
- `menu.buttonFleetManagement` – öffnet die Flottenverwaltung für ein kontrollierbares Objekt.
- `menu.createFleetUnitRow` – erzeugt eine UI-Zeile für eine Flotteneinheit.
- `menu.createSubordinateSection` – erstellt eine Unterabschnittsanzeige für Flotten oder Stationen.
