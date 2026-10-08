# Trust at Scale

Source for *Trust at Scale: Applied Cryptography from First Principles to the Post-Quantum Era* by Bolaji Akinyele.

- `src/` holds one Markdown file per chapter (`chNN.md`), the appendices (`appX.md`) and the preface.
- `build_book.py` turns the sources into a print-ready HTML book; `book.css` holds the design.
- `render.js` prints the HTML to PDF with Chromium (Playwright); `pagemap.py` finds page numbers for the contents page.

Build:

```bash
python3 build_book.py out
node render.js "$PWD/out/book.html" out/pass1.pdf
python3 pagemap.py out/pass1.pdf > out/map.json
python3 build_book.py out out/map.json
node render.js "$PWD/out/book.html" Trust-at-Scale.pdf
```
