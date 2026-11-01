"""Cartas de missão e sigilos de feitos no estilo do README do lich.

    python3 build_lich_extras.py <pasta-assets>
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

BG = "#0a0b0a"
LINE = "#2a2b26"
INK = "#e6e0cc"
MUTED = "#7d7a6e"
NEON = "#7cff4f"
DEEP = "#2f6e1c"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"

ICONS = {
    # g neon  G verde escuro  i creme  m cinza
    "torre": [
        "g.g.gg.g.g..",
        "gggggggggg..",
        ".iiiiiiii...",
        ".iimiiimi...",
        ".iiiiiiii...",
        ".iiiggiii...",
        ".iiiggiii...",
        ".iiiiiiii...",
        ".imiiiimi...",
        ".iiiGGiii...",
        ".iiiGGiii...",
        "mmmmmmmmmm..",
    ],
    "controle": [
        "............",
        "............",
        ".iiiiiiiiii.",
        "iiiiiiiiiiii",
        "iigiiiiiigii",
        "igggiiiigigi",
        "iigiiiiiigii",
        "iiiiimmiiiii",
        "iiiiiiiiiiii",
        ".iii....iii.",
        "............",
        "............",
    ],
    "cristal": [
        ".....gg.....",
        "....gggg....",
        "...ggGggg...",
        "..gggGgggg..",
        ".gggGggggGg.",
        ".ggGgggggGg.",
        "..gGgggggg..",
        "...gggggg...",
        "....gggg....",
        ".....gg.....",
        "...mmmmmm...",
        "..mmmmmmmm..",
    ],
    "pena": [
        "..........gg",
        ".........ggg",
        "........gggi",
        ".......gggi.",
        "......gggi..",
        ".....gggi...",
        "....gggi....",
        "...gGgi.....",
        "...Ggi......",
        "..mi........",
        ".m..........",
        "m...........",
    ],
    "runa": [
        "....gggg....",
        "..gg....gg..",
        ".g...ii...g.",
        ".g..i..i..g.",
        "g...i..i...g",
        "g....ii....g",
        "g.....i....g",
        "g....iii...g",
        ".g....i...g.",
        ".g........g.",
        "..gg....gg..",
        "....gggg....",
    ],
    "calice": [
        "..i.i.i.....",
        "...i.i......",
        "............",
        ".iiiiiiiii..",
        ".iggggggiimm",
        ".iggggggi..m",
        ".iggggggi..m",
        ".iiggggiimm.",
        "..iiiiii....",
        "...mmmm.....",
        "..mmmmmm....",
        "............",
    ],
    # sigilos dos feitos
    "varinha": [
        "........g...",
        ".......ggg.g",
        "........g...",
        "......i...g.",
        ".....i......",
        "....i.......",
        "...i........",
        "..m.........",
        ".m..........",
        "m...........",
        "............",
        "............",
    ],
    "grimorio": [
        ".GGGGGGGGGG.",
        "GggggggggggG",
        "GgiiiGGiiigG",
        "GgiiiGGiiigG",
        "GgmmmGGmmmgG",
        "GgiiiGGiiigG",
        "GgiiiGGiiigG",
        "GgmmmGGmmmgG",
        "GgiiiGGiiigG",
        "GggggggggggG",
        ".GGGGGGGGGG.",
        "............",
    ],
    "pinguim": [
        "....mmmm....",
        "...mmmmmm...",
        "...miimiim..",
        "...mmggmmm..",
        "..mmiiiimm..",
        ".mmiiiiiimm.",
        ".mmiiiiiimm.",
        ".mmiiiiiimm.",
        "..miiiiiim..",
        "...mmmmmm...",
        "..gg....gg..",
        "............",
    ],
    "dado": [
        ".....gg.....",
        "...gg..gg...",
        ".gg......gg.",
        "g..g....g..g",
        "g...gggg...g",
        "g..........g",
        "g..........g",
        "g..........g",
        "gg........gg",
        ".gg......gg.",
        "...gg..gg...",
        ".....gg.....",
    ],
}
COLORS = {"g": NEON, "G": DEEP, "i": INK, "m": MUTED}


def icon(name: str, x: float, y: float, s: int) -> str:
    out = []
    for ch, col in COLORS.items():
        d = "".join(
            f"M{x + c * s:g} {y + r * s:g}h{s}v{s}h-{s}z"
            for r, line in enumerate(ICONS[name]) for c, v in enumerate(line) if v == ch
        )
        if d:
            out.append(f'<path fill="{col}" d="{d}"/>')
    return "".join(out)


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


BASE_STYLE = """
    text { font-family: %s; }
    .pulse { animation: pulse 1.8s ease-out infinite; transform-box: fill-box; transform-origin: center; }
    @keyframes pulse { from { transform: scale(.6); opacity: .9 } to { transform: scale(2.2); opacity: 0 } }
    .spin { animation: spin 9s linear infinite; transform-box: fill-box; transform-origin: center; }
    @keyframes spin { to { transform: rotate(360deg) } }
    .glow { animation: glow 2.6s ease-in-out infinite alternate; }
    @keyframes glow { from { opacity: .35 } to { opacity: 1 } }
    @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
""" % MONO


# ── Cartas de missão ─────────────────────────────────────────────────────────
MISSOES = [
    ("I", "torre", "PDV para mercados", "caixa · estoque · NFC-e · quiosque", ["Go", "React", "Wails", "PostgreSQL"], "ativa"),
    ("II", "controle", "Masmorras de game dev", "protótipos e engines nas horas vagas", ["C++", "Rust"], "explorando"),
    ("III", "cristal", "mercado-ingestao", "ingestão de dados de mercado", ["Python"], "concluida"),
    ("IV", "pena", "gerador-exercicios", "gerador de exercícios", ["Python"], "concluida"),
    ("V", "runa", "node-typescript-api", "API em Node com TypeScript", ["Node.js", "TypeScript"], "concluida"),
    ("VI", "calice", "spring-boot-ionic-backend", "back-end REST", ["Java", "Spring Boot"], "concluida"),
]


def status_badge(kind: str, x: float, y: float) -> str:
    """Selo de status alinhado à direita em x (marca posicionada pelo tamanho do rótulo)."""
    label, col = {"ativa": ("EM ANDAMENTO", NEON), "explorando": ("EXPLORANDO", INK)}.get(kind, ("CONCLUÍDA", MUTED))
    mx = x - len(label) * 8.85 - 12
    my = y - 4
    if kind == "ativa":
        mark = (f'<circle class="pulse" cx="{mx}" cy="{my}" r="5" fill="none" stroke="{NEON}" stroke-width="1.5"/>'
                f'<circle cx="{mx}" cy="{my}" r="4" fill="{NEON}"/>')
    elif kind == "explorando":
        mark = f'<circle class="spin" cx="{mx}" cy="{my}" r="5" fill="none" stroke="{INK}" stroke-width="1.6" stroke-dasharray="3 2.5"/>'
    else:
        mark = (f'<circle cx="{mx}" cy="{my}" r="7" fill="{DEEP}"/>'
                f'<path d="M{mx - 3.5} {my}l2.5 2.5l4.5 -5" fill="none" stroke="{NEON}" stroke-width="1.8"/>')
    return mark + f'<text x="{x}" y="{y}" text-anchor="end" font-size="11" letter-spacing="2.2" fill="{col}">{label}</text>'


def card(num: str, ic: str, title: str, sub: str, stack: list[str], status: str) -> str:
    w, h = 500, 176
    chips, cxp = [], 104
    for t in stack:
        cw = len(t) * 7.6 + 18
        chips.append(
            f'<rect x="{cxp}" y="128" width="{cw:.0f}" height="24" rx="2" fill="{BG}" stroke="{LINE}" stroke-width="1.5"/>'
            f'<text x="{cxp + 9}" y="144" font-size="12" fill="{NEON}">{esc(t)}</text>'
        )
        cxp += cw + 8
    corner = lambda x, y, dx, dy: f'<path d="M{x} {y + 12 * dy}V{y}H{x + 12 * dx}" fill="none" stroke="{NEON}" stroke-width="2"/>'
    body = f"""
  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" fill="{BG}" stroke="{LINE}" stroke-width="2"/>
  {corner(6, 6, 1, 1)}{corner(w - 6, 6, -1, 1)}{corner(6, h - 6, 1, -1)}{corner(w - 6, h - 6, -1, -1)}
  <text x="28" y="36" font-size="11" letter-spacing="2.6" fill="{MUTED}">MISSÃO {num}</text>
  {status_badge(status, w - 28, 36)}
  <line x1="28" y1="50" x2="{w - 28}" y2="50" stroke="{LINE}" stroke-width="1.5"/>
  <rect x="28" y="64" width="60" height="60" fill="#0f110f" stroke="{LINE}" stroke-width="1.5"/>
  <g class="{'glow' if status == 'ativa' else ''}">{icon(ic, 34, 70, 4)}</g>
  <text x="104" y="86" font-size="20" font-weight="700" fill="{INK}">{esc(title)}</text>
  <text x="104" y="110" font-size="12.5" fill="{MUTED}">{esc(sub)}</text>
  {''.join(chips)}"""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="Missão {num}: {esc(title)}"><title>Missão {num}: {esc(title)}</title><style>{BASE_STYLE}</style>{body}\n</svg>\n')


# ── Sigilos de feitos ────────────────────────────────────────────────────────
FEITOS = [
    ("varinha", "O Primeiro Feitiço", "primeiro commit", "2016"),
    ("grimorio", "Mestre dos Grimórios", "Java · C# · Go · Python", "TypeScript · Rust · C++"),
    ("pinguim", "Guardião do Arch", "Arch Linux como", "sistema principal, btw"),
    ("torre", "Construtor de Fortalezas", "PDV em modo quiosque", "do banco ao boot"),
    ("dado", "Rolou 20 Natural", "nunca largou", "o controle"),
]


def feitos() -> str:
    w, h = 1000, 250
    col_w = w / len(FEITOS)
    parts = [f'<rect width="{w}" height="{h}" fill="{BG}"/>']
    for i, (ic, nome, l1, l2) in enumerate(FEITOS):
        cx = col_w * i + col_w / 2
        cy = 84
        delay = i * 0.5
        parts.append(f'<circle class="glow" style="animation-delay:-{delay}s" cx="{cx}" cy="{cy}" r="60" fill="{NEON}" fill-opacity=".10"/>')
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="52" fill="#0f110f" stroke="{DEEP}" stroke-width="2"/>')
        parts.append(f'<circle class="spin" style="animation-duration:{14 + i * 3}s" cx="{cx}" cy="{cy}" r="44" fill="none" '
                     f'stroke="{NEON}" stroke-width="1.5" stroke-dasharray="2 7" opacity=".8"/>')
        for k in range(4):  # marcas cardeais
            ang = ["M{0} {1}v8", "M{0} {1}v-8", "M{0} {1}h8", "M{0} {1}h-8"][k]
            px, py = [(cx, cy - 52), (cx, cy + 52), (cx - 52, cy), (cx + 52, cy)][k]
            parts.append(f'<path d="{ang.format(px, py)}" stroke="{NEON}" stroke-width="2"/>')
        if ic == "dado":
            parts.append(f'<g class="glow">{icon(ic, cx - 24, cy - 24, 4)}'
                         f'<text x="{cx}" y="{cy + 7}" text-anchor="middle" font-size="17" font-weight="800" fill="{INK}">20</text></g>')
        else:
            parts.append(icon(ic, cx - 24, cy - 24, 4))
        parts.append(f'<text x="{cx}" y="176" text-anchor="middle" font-size="14" font-weight="700" fill="{INK}">{esc(nome)}</text>')
        parts.append(f'<text x="{cx}" y="200" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(l1)}</text>')
        parts.append(f'<text x="{cx}" y="218" text-anchor="middle" font-size="11.5" fill="{MUTED}">{esc(l2)}</text>')
        if i:
            parts.append(f'<line x1="{col_w * i}" y1="40" x2="{col_w * i}" y2="200" stroke="{LINE}" stroke-width="1.5"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="Feitos lendários: {", ".join(f[1] for f in FEITOS)}"><title>Feitos lendários</title>'
            f'<style>{BASE_STYLE}</style>{"".join(parts)}\n</svg>\n')


for i, m in enumerate(MISSOES, 1):
    (OUT / f"missao-{i}.svg").write_text(card(*m), encoding="utf-8")
(OUT / "feitos.svg").write_text(feitos(), encoding="utf-8")
print("ok")
