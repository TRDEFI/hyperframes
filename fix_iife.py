import os, re

compositions_dir = r"C:\Users\cemya\.openclaw\workspace\hyperframes\compositions"

for fname in os.listdir(compositions_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(compositions_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only fix files that have "const tl = gsap.timeline" in their script
    if 'const tl = gsap.timeline' not in content:
        print(f"{fname}: NO const tl — skipping")
        continue

    # Wrap the script block in an IIFE to isolate `const tl`
    # Find the script block that contains "const tl = gsap.timeline"
    # We wrap the entire script content after the opening <script>
    new_content = re.sub(
        r'(<script>)(window\.__timelines = window\.__timelines \|\| \{\};)',
        r'\1\2; (function(){',
        content
    )
    # Close the IIFE before the closing </script>
    new_content = re.sub(
        r'(window\.__timelines\[[^\]]+\] = tl;)(\s*)(</script>)',
        r'\1\2})();\3',
        new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"{fname}: wrapped in IIFE")