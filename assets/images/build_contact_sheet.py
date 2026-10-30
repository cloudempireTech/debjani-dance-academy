import os
from PIL import Image

img_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\debjani-dance-academy\assets\images"
files = [f for f in os.listdir(img_dir) if f.startswith("photo_") and f.endswith(".jpg")]
files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

html = ["<html><body style='background:#111;color:#fff;font-family:sans-serif;padding:20px;'><h1 style='color:#f43f5e;'>Debjani Dance Academy - Scraped Verified Photos</h1><div style='display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:20px;'>"]

for f in files:
    p = os.path.join(img_dir, f)
    with Image.open(p) as img:
        w, h = img.size
        sz = os.path.getsize(p) // 1024
    html.append(f"<div style='background:#222;padding:10px;border-radius:8px;'>")
    html.append(f"<img src='{f}' style='width:100%;height:220px;object-fit:cover;border-radius:6px;'/>")
    html.append(f"<p style='margin:5px 0 0 0;font-size:12px;color:#ccc;'><b>{f}</b>: {w}x{h} ({sz} KB)</p>")
    html.append(f"</div>")

html.append("</div></body></html>")

with open(os.path.join(img_dir, "contact_sheet.html"), "w") as f_out:
    f_out.write("\n".join(html))

print("Created contact_sheet.html with", len(files), "photos.")
