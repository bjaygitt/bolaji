"""Find the page of each @@KEY@@ marker in a rendered PDF. Usage: python3 pagemap.py book.pdf > map.json"""
import json, re, subprocess, sys

pdf = sys.argv[1]
text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
result = {}
for i, page in enumerate(text.split("\f"), start=1):
    for key in re.findall(r"@@([A-Z]\w*)@@", page):
        result.setdefault(key, i)
print(json.dumps(result))
