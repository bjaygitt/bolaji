// Render book.html to PDF with Chromium. Usage: node render.js <in.html> <out.pdf>
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + process.argv[2], { waitUntil: 'load', timeout: 300000 });
  await page.pdf({ path: process.argv[3], preferCSSPageSize: true, printBackground: true, outline: true, tagged: true, timeout: 600000 });
  await browser.close();
})();
