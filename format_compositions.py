import os, re

comp_dir = r"C:\Users\cemya\.openclaw\workspace\hyperframes\compositions"

for fname in sorted(os.listdir(comp_dir)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(comp_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split on </script> and rejoin with newlines
    parts = content.split('</script>')
    formatted = ('</script>\n').join(parts)

    # Also add newlines around major structural tags for readability
    for tag in ['<html', '<head', '<body', '<style', '</style>', '<script>']:
        formatted = formatted.replace(tag, '\n' + tag)
    for tag in ['</head>', '</body>', '</html>']:
        formatted = formatted.replace(tag, '\n' + tag)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(formatted)

    lines = formatted.count('\n') + 1
    print(f"{fname}: {lines} lines, {len(formatted)} chars")
