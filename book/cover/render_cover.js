const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 672, height: 883 }, deviceScaleFactor: 3 });
  await p.goto('file://' + process.argv[2], { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[3], width: '7in', height: '9.19in', printBackground: true, preferCSSPageSize: true });
  await p.screenshot({ path: process.argv[4], clip: { x: 0, y: 0, width: 672, height: 882.24 } });
  await b.close();
})();
