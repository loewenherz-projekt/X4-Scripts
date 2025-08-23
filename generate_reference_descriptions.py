import re, io

def camel_to_words(s: str) -> str:
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', s)
    s = s.replace('_', ' ')
    return s.lower()


def xml_description(cmd, attrs):
    base = cmd
    if base.startswith('find_'):
        text = f"Sucht {base[5:].replace('_', ' ')}"
    elif base.startswith('add_'):
        text = f"Fügt {base[4:].replace('_', ' ')} hinzu"
    elif base.startswith('remove_'):
        text = f"Entfernt {base[7:].replace('_', ' ')}"
    elif base.startswith('set_'):
        text = f"Setzt {base[4:].replace('_', ' ')}"
    elif base.startswith('get_'):
        text = f"Gibt {base[4:].replace('_', ' ')} zurück"
    elif base.startswith('abort_'):
        text = f"Bricht {base[6:].replace('_', ' ')} ab"
    elif base.startswith('activate_'):
        text = f"Aktiviert {base[9:].replace('_', ' ')}"
    elif base.startswith('deactivate_'):
        text = f"Deaktiviert {base[11:].replace('_', ' ')}"
    else:
        text = base.replace('_', ' ').capitalize()
    if attrs:
        text += f" (Attribute: {', '.join(attrs)})"
    return text + '.'


def lua_description(funcname, params):
    base = funcname.split('.')[-1]
    words = camel_to_words(base)
    if words.startswith('get '):
        text = f"Gibt {words[4:]} zurück"
    elif words.startswith('set '):
        text = f"Setzt {words[4:]}"
    elif words.startswith('add '):
        text = f"Fügt {words[4:]} hinzu"
    elif words.startswith('remove '):
        text = f"Entfernt {words[7:]}"
    elif words.startswith('is '):
        text = f"Prüft ob {words[3:]}"
    else:
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
