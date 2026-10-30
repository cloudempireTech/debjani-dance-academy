const fs = require('fs');
const path = require('path');

const baseDir = __dirname;
const htmlFiles = ['index.html', 'about.html', 'offerings.html', 'catering.html', 'gallery.html', 'reviews.html', 'contact.html'];

let totalChecked = 0;
let errors = 0;

htmlFiles.forEach(file => {
  const filePath = path.join(baseDir, file);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing HTML file: ${file}`);
    errors++;
    return;
  }

  const content = fs.readFileSync(filePath, 'utf8');

  // Regex to extract all img src and video poster and video source
  const srcMatches = content.matchAll(/(?:src|poster)=["']([^"']+)["']/g);
  for (const match of srcMatches) {
    const assetPath = match[1];
    // Ignore external URLs or inline data
    if (assetPath.startsWith('http://') || assetPath.startsWith('https://') || assetPath.startsWith('data:')) {
      continue;
    }

    totalChecked++;
    const fullAssetPath = path.resolve(baseDir, assetPath);
    if (!fs.existsSync(fullAssetPath)) {
      console.error(`[${file}] Missing asset: ${assetPath} (Resolved: ${fullAssetPath})`);
      errors++;
    } else {
      const stats = fs.statSync(fullAssetPath);
      if (stats.size === 0) {
        console.error(`[${file}] Empty file (0 bytes): ${assetPath}`);
        errors++;
      }
    }
  }
});

console.log(`\n=== ASSET VERIFICATION REPORT ===`);
console.log(`Total local assets checked across 7 HTML pages: ${totalChecked}`);
console.log(`Errors / Missing assets: ${errors}`);

if (errors > 0) {
  console.error(`FAILED: ${errors} missing or broken assets detected!`);
  process.exit(1);
} else {
  console.log(`SUCCESS: All ${totalChecked} assets verified to exist with non-zero size! ZERO missing images.`);
  process.exit(0);
}
