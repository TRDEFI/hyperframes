import re

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix viewport
content = content.replace(
    '<meta name="viewport" content="width=device=link">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">'
)

# Add data attributes to composition div
content = content.replace(
    '<div class="composition" id="comp">',
    '<div class="composition" id="comp" data-composition-id="detective-pikachu" data-width="1080" data-height="1920">'
)

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
print("comp-id:", "data-composition-id" in content)
print("data-width:", "data-width" in content)
print("data-height:", "data-height" in content)
print("viewport:", "viewport" in content)