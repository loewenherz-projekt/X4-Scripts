import re, io

def camel_to_words(s: str) -> str:
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', s)
    s = s.replace('_', ' ')
    return s.lower()


def xml_description(cmd, attrs):
    base = cmd
    prefix_map = {
        'find_': 'Sucht {}',
        'add_': 'Fügt {} hinzu',
        'remove_': 'Entfernt {}',
        'set_': 'Setzt {}',
        'get_': 'Gibt {} zurück',
        'abort_': 'Bricht {} ab',
        'activate_': 'Aktiviert {}',
        'deactivate_': 'Deaktiviert {}',
        'update_': 'Aktualisiert {}',
        'toggle_': 'Schaltet {} um',
        'close_': 'Schließt {}',
        'open_': 'Öffnet {}',
        'start_': 'Startet {}',
        'stop_': 'Stoppt {}',
        'clear_': 'Leert {}',
        'reset_': 'Setzt {} zurück',
        'calculate_': 'Berechnet {}',
        'create_': 'Erstellt {}',
        'destroy_': 'Zerstört {}',
        'show_': 'Zeigt {}',
        'hide_': 'Versteckt {}',
        'move_': 'Bewegt {}',
        'select_': 'Wählt {} aus',
        'apply_': 'Wendet {} an',
        'load_': 'Lädt {}',
        'save_': 'Speichert {}',
        'spawn_': 'Erzeugt {}',
        'lock_': 'Sperrt {}',
        'unlock_': 'Entsperrt {}',
        'enable_': 'Aktiviert {}',
        'disable_': 'Deaktiviert {}',
        'event_': 'Wird ausgelöst, wenn {}',
    }
    text = None
    for prefix, template in prefix_map.items():
        if base.startswith(prefix):
            rest = base[len(prefix):].replace('_', ' ')
            text = template.format(rest)
            break
    if text is None:
        text = base.replace('_', ' ').capitalize()
    if attrs:
        text += f" (Attribute: {', '.join(attrs)})"
    return text + '.'


def lua_description(funcname, params):
    base = funcname.split('.')[-1]
    words = camel_to_words(base)
    prefix_map = {
        'get ': 'Gibt {} zurück',
        'set ': 'Setzt {}',
        'add ': 'Fügt {} hinzu',
        'remove ': 'Entfernt {}',
        'is ': 'Prüft ob {}',
        'update ': 'Aktualisiert {}',
        'toggle ': 'Schaltet {} um',
        'draw ': 'Zeichnet {}',
        'close ': 'Schließt {}',
        'open ': 'Öffnet {}',
        'start ': 'Startet {}',
        'stop ': 'Stoppt {}',
        'clear ': 'Leert {}',
        'reset ': 'Setzt {} zurück',
        'calculate ': 'Berechnet {}',
        'create ': 'Erstellt {}',
        'destroy ': 'Zerstört {}',
        'show ': 'Zeigt {}',
        'hide ': 'Versteckt {}',
        'move ': 'Bewegt {}',
        'select ': 'Wählt {} aus',
        'apply ': 'Wendet {} an',
        'load ': 'Lädt {}',
        'save ': 'Speichert {}',
        'activate ': 'Aktiviert {}',
        'deactivate ': 'Deaktiviert {}',
    }
    text = None
    for prefix, template in prefix_map.items():
        if words.startswith(prefix):
            text = template.format(words[len(prefix):])
            break
    if text is None:
        text = f"Führt {words} aus"
    if params:
        text += f" (Parameter: {', '.join(params)})"
    return text + '.'


def parse_xml_example(cmd, filepath):
    attrs = []
    try:
        with io.open(filepath, encoding='utf-8') as f:
            for line in f:
                if re.search(r'<\s*' + re.escape(cmd) + r'\b', line):
                    attrs = re.findall(r'(\w+)=', line)
                    break
    except FileNotFoundError:
        pass
    return xml_description(cmd, attrs)


def parse_lua_example(funcname, filepath):
    params = []
    try:
        with io.open(filepath, encoding='utf-8') as f:
            for line in f:
                if re.search(r'^\s*function\s+' + re.escape(funcname) + r'\s*\(', line):
                    param_str = re.search(r'\(([^)]*)\)', line)
                    if param_str:
                        params = [p.strip() for p in param_str.group(1).split(',') if p.strip()]
                    break
    except FileNotFoundError:
        pass
    return lua_description(funcname, params)


def update_reference(filename, kind):
    with io.open(filename, encoding='utf-8') as f:
        lines = f.read().splitlines()
    header = lines[:4]
    entries = [l for l in lines[6:] if l.startswith('|')]
    if kind == 'xml':
        new_header = ['| Befehl | Vorkommen | Beispieldatei | Beschreibung |', '| --- | --- | --- | --- |']
    else:
        new_header = ['| Funktion | Vorkommen | Beispieldatei | Beschreibung |', '| --- | --- | --- | --- |']
    new_lines = header + new_header
    for line in entries:
        parts = [p.strip() for p in line.strip().split('|')[1:-1]]
        if len(parts) < 3:
            continue
        name, count, file = parts[:3]
        name_clean = name.strip('`')
        file_clean = file.strip('`')
        if kind == 'xml':
            desc = parse_xml_example(name_clean, file_clean)
        else:
            desc = parse_lua_example(name_clean, file_clean)
        new_lines.append(f"| {name} | {count} | `{file_clean}` | {desc} |")
    with io.open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines) + '\n')

if __name__ == '__main__':
    update_reference('SCRIPT_COMMAND_REFERENCE.md', 'xml')
    update_reference('LUA_FUNCTION_REFERENCE.md', 'lua')
