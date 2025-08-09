"""
restore_logo_square.py

Reads the original logo PNG and re-generates assets/logo_square.svg by embedding the PNG as a 512x512 SVG.
"""
import base64
from pathlib import Path

# Paths
assets = Path(__file__).parent.parent / 'assets'
orig_png = assets / 'logo_orig.png'
out_svg = assets / 'logo_square.svg'

# Read and encode PNG
data = orig_png.read_bytes()
b64 = base64.b64encode(data).decode('utf-8')

# Generate SVG wrapper
svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="512" height="512" viewBox="0 0 512 512">
  <image width="512" height="512" xlink:href="data:image/png;base64,{b64}" />
</svg>
'''

# Write SVG
out_svg.write_text(svg_content, encoding='utf-8')
print(f"Restored embedding PNG from {orig_png.name} into {out_svg.name}")
