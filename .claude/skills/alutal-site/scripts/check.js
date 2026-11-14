// Smoke test: opens every view at desktop (dark) and phone (light) width,
// reports console errors, horizontal overflow and missing images.
// Usage: node .claude/skills/alutal-site/scripts/check.js [screenshotDir]
const {chromium} = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '../../../..');
const out = process.argv[2];
const VIEWS = ['home','about','services','projects','specs','contact'];
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w,h,name,scheme] of [[1440,900,'desktop','dark'],[390,844,'phone','light']]) {
    const pg = await b.newPage({viewport:{width:w,height:h}, colorScheme:scheme});
    pg.on('pageerror', e => errs.push(e.message));
    pg.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    pg.on('requestfailed', r => errs.push('missing: ' + r.url().replace(/^.*\/img\//,'img/')));
    await pg.goto('file://' + root + '/index.html#home'); await pg.waitForTimeout(600);
    for (const v of VIEWS) {
      await pg.evaluate(v => location.hash = v, v); await pg.waitForTimeout(400);
      await pg.evaluate(async () => { for (let y=0; y<document.body.scrollHeight; y+=800){ scrollTo(0,y); await new Promise(r=>setTimeout(r,40)); } });
      const sw = await pg.evaluate(() => document.documentElement.scrollWidth);
      if (sw > w) console.log('OVERFLOW', name, v, sw);
      if (out) await pg.screenshot({path: `${out}/${name}_${v}.png`, fullPage: true});
    }
  }
  console.log('errors', [...new Set(errs)]); await b.close();
})();
