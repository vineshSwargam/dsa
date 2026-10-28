# Embeds the solution files linked from constants.js into tracker.html,
# since a local HTML file can't read other local files.
# Re-run after editing or adding a solution: python tracker/sync_tracker.py

import json
import re
from pathlib import Path

HERE = Path(__file__).parent  # solution paths are relative to this folder
TRACKER = HERE / "tracker.html"
CONSTANTS = HERE / "constants.js"

html = TRACKER.read_text()

# Every file path listed in the PROBLEMS table
paths = re.findall(r'^\s*\[".*?", "\w+", "([^"]+)"\],?$', CONSTANTS.read_text(), re.M)

sources = {}
for p in paths:
    f = HERE / p
    if f.is_file():
        sources[p] = f.read_text()
    else:
        print("missing:", p)

# "</" would end the <script> tag early, so escape it inside the JSON
blob = json.dumps(sources).replace("</", "<\\/")

html, n = re.subn(
    r'(<script id="sources" type="application/json">).*?(</script>)',
    lambda m: m.group(1) + blob + m.group(2),
    html,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit("couldn't find the sources block in tracker.html")

TRACKER.write_text(html)
print(f"embedded {len(sources)} files")
