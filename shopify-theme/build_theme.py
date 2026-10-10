#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent / 'perrijo-gatijo-shopify-theme.zip'
REQUIRED = ('assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates')

missing = [name for name in REQUIRED if not (ROOT / name).is_dir()]
if missing:
    raise SystemExit('Faltan carpetas requeridas: ' + ', '.join(missing))
with ZipFile(OUTPUT, 'w', ZIP_DEFLATED) as archive:
    for folder in REQUIRED:
        for path in sorted((ROOT / folder).rglob('*')):
            if path.is_file():
                archive.write(path, path.relative_to(ROOT).as_posix())
print(OUTPUT)
