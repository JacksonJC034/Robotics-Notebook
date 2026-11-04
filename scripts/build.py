import json, subprocess, sys
from pathlib import Path
p=Path(__file__).resolve().parents[1]
records=json.loads((p/'catalog.json').read_text())
for r in records:
 r['body']=(p/'docs'/r['path'].replace('.html','.md')).read_text()
(p/'docs/_static/catalog-data.js').write_text('window.NOTEBOOK_CATALOG='+json.dumps(records,ensure_ascii=False)+';')
subprocess.run([sys.executable,'-m','sphinx','-W','--keep-going','-b','html',str(p/'docs'),str(p/'dist')],check=True)
(p/'dist/.nojekyll').touch()
