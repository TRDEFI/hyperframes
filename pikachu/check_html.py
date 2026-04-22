import re

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = {
    'data-composition-id': 'data-composition-id' in content,
    'data-width': 'data-width' in content,
    'data-height': 'data-height' in content,
    'class=composition': 'class="composition"' in content,
    'id=comp': 'id="comp"' in content,
    'viewport': 'viewport' in content,
}

for k, v in checks.items():
    print(f"{'OK' if v else 'MISSING'}: {k}")

# Check for duplicate data-width or data-height (should be on root only)
root_matches = re.findall(r'data-width="1080"', content)
print(f"\ndata-width occurrences: {len(root_matches)} (should be 1)")

# Check for viewport content
vp = re.search(r'content="width=device-width', content)
print(f"viewport: {'OK' if vp else 'MISSING'}")