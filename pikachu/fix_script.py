import re

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix root element: add data-start and data-duration
content = content.replace(
    '<div class="composition" id="comp" data-composition-id="detective-pikachu" data-width="1080" data-height="1920">',
    '<div class="composition" id="comp" data-composition-id="detective-pikachu" data-width="1080" data-height="1920" data-start="0" data-duration="23">'
)

# 2. Find and replace the old script block with the new one
# The old script starts with: <script> and ends with: </script>
old_script_match = re.search(r'<script>\s*\(function\(\)\s*\{', content)
if old_script_match:
    # Find the matching </script>
    script_start = old_script_match.start()
    script_end = content.find('</script>', script_start)
    if script_end != -1:
        new_script = open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\js_footer.txt', 'r', encoding='utf-8').read()
        content = content[:script_start] + '<script>\n' + new_script + '\n' + content[script_end + len('</script>'):]
        print("Replaced script block")
    else:
        print("WARNING: No closing script tag found")
else:
    print("WARNING: Old script pattern not found")

# 3. Remove any trailing content after </html>
if '</html>' in content:
    content = content.split('</html>')[0] + '</html>\n'

with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Total length:", len(content))

# Verify
with open(r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\index.html', 'r', encoding='utf-8') as f:
    final = f.read()
print("data-start:", 'data-start' in final)
print("data-duration:", 'data-duration' in final)
print("window.__hf:", 'window.__hf' in final)
print("mulberry32:", 'mulberry32' in final)
print("performance.now:", 'performance.now' in final)
print("Last 50 chars:", repr(final[-50:]))