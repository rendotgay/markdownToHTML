import re

from codeblocks import toggle_inline, LANGUAGES


def headers(line):
    if "### " in line:
        return f"<h3>{line.split('### ')[1]}</h3>"
    elif "## " in line:
        return f"<h2>{line.split('## ')[1]}</h2>\n<hr>"
    elif "# " in line:
        return f"<h1>{line.split('# ')[1]}</h1>\n<hr>"
    else:
        return line


def lists(line):
    if "- " in line:
        return f"<li>{line.split('- ')[1]}</li>"
    match = re.search(r"(\d+)\.\s*(.*)", line)
    if match:
        return f'<li value="{match.group(1)}">{match.group(2)}</li>'
    else:
        return line


def anchors(line):
    return re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', line)


def parse(content, css:bool, gsc:bool = False):
    html = []
    ul = False
    ol = False
    code_block = False
    code_block_spaces = 0
    code_block_tabs = 0
    code_block_open_tag = ""
    for line in content.split('\n'):
        stripped = line.strip()
        match = re.match(r"^\s*", line).group()
        spaces = match.count(" ")
        tabs = match.count("\t")
        spaces += tabs * 4

        # Codeblocks
        if stripped.startswith("```"):
            if not code_block:
                if ul:
                    html.append('</ul>')
                    ul = False
                if ol:
                    html.append('</ol>')
                    ol = False
                code_block_spaces = spaces
                code_block_tabs = tabs
                tag = stripped[3:].strip().lower()
                lang = tag if tag in LANGUAGES else ""
                if gsc and lang in ['c', 'cpp', 'c++', 'csharp', 'c#']:
                    lang = 'gsc'
                code_block = True
                code_block_open_tag = f'<pre style="margin-left: {spaces * 10}px;"><code class="block{" language-" + lang if lang else ""}">'
            else:
                html.append('</code></pre>')
                code_block = False
                code_block_open_tag = ""
            continue

        if code_block:
            if line.startswith("\t" * code_block_tabs):
                line = line[code_block_tabs:]
            elif line.startswith(" " * code_block_spaces):
                line = line[code_block_spaces:]
            escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            if code_block_open_tag:
                html.append(code_block_open_tag + escaped)
                code_block_open_tag = ""
            else:
                html.append(escaped)
            continue

        # Headers
        if stripped.startswith('#'):
            line = headers(line)

        # Lists
        if stripped.startswith('-'):
            if not ul:
                html.append('<ul>')
            line = lists(line)
            ul = True
        elif ul:
            ul = False
            html.append('</ul>')
        if re.match(r"\d+\.", stripped):
            if not ol:
                html.append('<ol>')
            line = lists(line)
            ol = True
        elif ol:
            ol = False
            html.append('</ol>')

        # Anchors
        if all(char in line for char in ["[", "(", "]", ")"]):
            line = anchors(line)

        # Add spacing
        if not ul and not ol and not code_block and css and spaces:
            line = f'<div style="padding-left: {spaces * 10}px;">{line}</div>'

        # Inline codeblocks
        if "`" in line and "```" not in line:
            line = re.sub(r"`", toggle_inline, line)

        # Add to HTML
        html.append(line)

    return html