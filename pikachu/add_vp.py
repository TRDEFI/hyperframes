with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find line 4 (index 3) and add viewport meta after charset
new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    if i == 2 and '<meta charset' in line:  # after charset line
        new_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1">\n')

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done, lines:", len(new_lines))