with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Add viewport as second meta tag (after charset)
if 'viewport' not in content:
    parts = content.split('<title>', 1)
    viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    content = parts[0] + viewport_meta + '<title>' + parts[1]

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
print('viewport:', 'viewport' in open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', encoding='utf-8').read())