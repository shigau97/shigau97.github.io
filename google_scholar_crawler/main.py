from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import sys

"""
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shields# new / replace near the top
"""

# choose ID: CLI -> gs_id.txt -> env
GS_ID = None
if len(sys.argv) > 1:
    GS_ID = sys.argv[1].strip()
else:
    try:
        with open('gs_id.txt', 'r', encoding='utf-8') as f:
            GS_ID = f.read().strip()
    except FileNotFoundError:
        GS_ID = os.environ.get('GOOGLE_SCHOLAR_ID')

if not GS_ID:
    print('ERROR: Google Scholar ID not provided. Provide as CLI arg, gs_id.txt, or set GOOGLE_SCHOLAR_ID', file=sys.stderr)
    sys.exit(1)

author: dict = scholarly.search_author_id(GS_ID)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author.get('name', '')
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author.get('publications', [])}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author.get('citedby', 0)}",
}
with open('results/gs_data_shieldsio.json', 'w', encoding='utf-8') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)