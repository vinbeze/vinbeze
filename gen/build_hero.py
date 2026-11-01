"""Junta o terminal (title.svg) e o lich (PNG) num único hero.svg, com o lich
invadindo a borda direita do terminal.

    python3 build_hero.py <title.svg> <lich.png> <saida.svg> [sobreposicao_px]
"""
import base64
import re
import subprocess
import sys

title_path, lich_path, out_path = sys.argv[1:4]
overlap = float(sys.argv[4]) if len(sys.argv) > 4 else 70

# terminal: remove metadados e transforma a raiz num <svg> aninhado
t = open(title_path, encoding="utf-8").read()
t = re.sub(r"<metadata>.*?</metadata>", "", t, flags=re.S)
m = re.search(r"<svg\b[^>]*>", t)
tw, th = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', m.group(0)).groups())
inner = t[m.end():t.rindex("</svg>")]
# evita colisão de ids entre o terminal e o resto do hero
inner = re.sub(r'id="([^"]+)"', r'id="t-\1"', inner)
inner = re.sub(r"url\(#([^)]+)\)", r"url(#t-\1)", inner)
inner = re.sub(r'href="#([^"]+)"', r'href="#t-\1"', inner)

# lich: 560px, paleta de 256 cores, PNG em base64
png = subprocess.run(
    ["magick", lich_path, "-resize", "560x560", "-colors", "256", "-define", "png:compression-level=9", "png:-"],
    capture_output=True, check=True).stdout
b64 = base64.b64encode(png).decode()

pad = 24                      # respiro em cima para a coroa passar da borda
lh = th + pad                 # lich um pouco mais alto que o terminal
lw = lh                       # imagem quadrada
lx = tw - overlap             # invade a borda direita do terminal
W = lx + lw                   # largura total (o cajado vai até a borda da imagem)
H = th + pad

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="Vinbeze — necromante de software desde 2016, com o lich coroado segurando uma chama verde e um cajado de caveira">
  <title>Vinbeze — necromante de software desde 2016</title>
  <defs>
    <radialGradient id="h-aura" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#7cff4f" stop-opacity=".22"/>
      <stop offset="1" stop-color="#7cff4f" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .aura {{ animation: aura 3.2s ease-in-out infinite alternate; }}
    @keyframes aura {{ from {{ opacity: .45 }} to {{ opacity: 1 }} }}
    @media (prefers-reduced-motion: reduce) {{ .aura {{ animation: none; }} }}
  </style>
  <svg x="0" y="{pad}" width="{tw:g}" height="{th:g}" viewBox="0 0 {tw:g} {th:g}">{inner}</svg>
  <ellipse class="aura" cx="{lx + lw * 0.47:.0f}" cy="{H - 14:.0f}" rx="{lw * 0.42:.0f}" ry="26" fill="url(#h-aura)"/>
  <image x="{lx:.0f}" y="0" width="{lw:.0f}" height="{lh:.0f}" href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}"/>
</svg>
"""
open(out_path, "w", encoding="utf-8").write(svg)
print(f"hero {W:.0f}x{H:.0f}, png {len(png) // 1024} KB, svg {len(svg) // 1024} KB")
