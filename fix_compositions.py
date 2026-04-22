import os, re

comp_dir = r"C:\Users\cemya\.openclaw\workspace\hyperframes\compositions"

for fname in sorted(os.listdir(comp_dir)):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(comp_dir, fname)

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The fix_iife.py corrupted the structure by placing window.__timelines OUTSIDE the IIFE.
    # Fix: move window.__timelines registration INSIDE the IIFE.
    #
    # Current (broken) pattern:
    #   window.__timelines = window.__timelines || {};
    #   (function(){
    #   const tl = gsap.timeline({...});
    #   ... code ...
    #   window.__timelines['beatX'] = tl;  })();  <-- AFTER IIFE closes!
    #   </script>
    #
    # Desired pattern: window.__timelines registration stays inside IIFE
    #   (function(){
    #   const tl = gsap.timeline({...});
    #   ... code ...
    #   window.__timelines['beatX'] = tl;
    #   })();

    # Strategy: find the window.__timelines assignment that's BEFORE the </script>
    # and move it to just before the closing })();
    # Also remove the erroneous })(); that's after window.__timelines assignment.

    # Find all window.__timelines registrations
    tl_assign_pattern = r"(window\.__timelines\['(beat\d+)'\]\s*=\s*tl;)"
    matches = list(re.finditer(tl_assign_pattern, content))

    if not matches:
        print(f"{fname}: no timeline registration found - skipping")
        continue

    # The tl registration should be the LAST window.__timelines['beatX'] = tl; before </script>
    # Find the last one before </script>
    last_tl = None
    for m in reversed(matches):
        pos = m.start()
        # Make sure it's before </script>
        script_end = content.find('</script>', pos)
        if script_end > pos:
            last_tl = m
            break

    if not last_tl:
        print(f"{fname}: timeline registration not found before </script>")
        continue

    beat_id = last_tl.group(2)
    tl_assign = last_tl.group(1)  # e.g. "window.__timelines['beat1'] = tl;"

    # Now find the )}); that closes the IIFE - look for pattern:
    # window.__timelines['beatX'] = tl;  })();
    # The })(); should be AFTER tl assignment
    broken_pattern = re.escape(tl_assign) + r"\s*\}\)\(\);"
    broken_match = re.search(broken_pattern, content)

    if broken_match:
        # This is the broken pattern - fix it
        # Replace: window.__timelines['beatX'] = tl;  })();
        # With: window.__timelines['beatX'] = tl;\n    })\();
        # Wait - actually we need the tl assignment INSIDE the IIFE
        # The current structure has tl assignment AFTER })();
        # We need to swap them: put tl assignment BEFORE the })();
        old = broken_match.group(0)
        new = "    " + tl_assign + "\n    });"
        content = content.replace(old, new, 1)
        print(f"{fname}: fixed IIFE structure for {beat_id}")
    else:
        print(f"{fname}: IIFE structure OK for {beat_id}, checking...")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
