"""Gera os SVGs do README de perfil (tema: RPG retrô em tela CRT).

    python3 -I build.py <pasta-de-saida>
"""
import random
import sys
from pathlib import Path

from pixelfont import sprite_path, text_path, text_width

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

# Paleta: fósforo âmbar + ciano/magenta de aberração cromática.
BG = "#06070c"
SCREEN = "#0b0e17"
BEZEL = "#151826"
AMBER = "#ffb547"
AMBER_DIM = "#8a5f23"
CYAN = "#4ff0ff"
MAGENTA = "#ff4f8b"
GREEN = "#7dff8a"
DIM = "#3a4256"
INK = "#e9e3d3"

W = 960


def center_x(text: str, scale: int, width: int = W) -> float:
    return (width - text_width(text, scale)) / 2


def crt_defs(w: int, h: int, uid: str) -> str:
    """Scanlines, vinheta e brilho de fósforo compartilhados pelos SVGs."""
    return f"""
  <defs>
    <pattern id="scan-{uid}" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="2" fill="#000" opacity="0.32"/>
    </pattern>
    <radialGradient id="vig-{uid}" cx="50%" cy="50%" r="75%">
      <stop offset="60%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.75"/>
    </radialGradient>
    <radialGradient id="glow-{uid}" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="{AMBER}" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="{AMBER}" stop-opacity="0"/>
    </radialGradient>
    <filter id="bloom-{uid}" x="-10%" y="-30%" width="120%" height="160%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="clip-{uid}"><rect x="18" y="18" width="{w - 36}" height="{h - 36}" rx="22"/></clipPath>
  </defs>"""


def screen_frame(w: int, h: int, uid: str) -> tuple[str, str]:
    """Moldura do monitor (abertura) e camadas por cima do conteúdo (fechamento)."""
    abre = f"""
  <rect width="{w}" height="{h}" rx="30" fill="{BEZEL}"/>
  <rect x="6" y="6" width="{w - 12}" height="{h - 12}" rx="26" fill="none" stroke="#232741" stroke-width="2"/>
  <rect x="18" y="18" width="{w - 36}" height="{h - 36}" rx="22" fill="{SCREEN}"/>
  <g clip-path="url(#clip-{uid})">
    <rect x="18" y="18" width="{w - 36}" height="{h - 36}" fill="url(#glow-{uid})"/>"""
    fecha = f"""
    <rect x="18" y="18" width="{w - 36}" height="{h - 36}" fill="url(#scan-{uid})"/>
    <rect class="roll" x="18" y="-60" width="{w - 36}" height="60" fill="#fff" opacity="0.035"/>
    <rect x="18" y="18" width="{w - 36}" height="{h - 36}" fill="url(#vig-{uid})"/>
  </g>
  <rect x="18" y="18" width="{w - 36}" height="{h - 36}" rx="22" fill="none" stroke="#000" stroke-opacity="0.6" stroke-width="3"/>"""
    return abre, fecha


def stars(n: int, w: int, h: int, seed: int, top: int = 24) -> str:
    rnd = random.Random(seed)
    out = []
    for i in range(n):
        x = rnd.randint(30, w - 30)
        y = rnd.randint(top, h - 30)
        s = rnd.choice([2, 2, 2, 3])
        d = rnd.uniform(1.5, 4.5)
        delay = rnd.uniform(0, 4)
        color = rnd.choice([INK, INK, CYAN, AMBER])
        out.append(
            f'<rect class="tw" x="{x}" y="{y}" width="{s}" height="{s}" fill="{color}" '
            f'style="animation-duration:{d:.1f}s;animation-delay:-{delay:.1f}s"/>'
        )
    return "\n    ".join(out)


def svg(w: int, h: int, title: str, style: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
  <title>{title}</title>
  <style>
    .tw {{ animation: tw ease-in-out infinite alternate; }}
    @keyframes tw {{ from {{ opacity: .15 }} to {{ opacity: 1 }} }}
    .roll {{ animation: roll 7s linear infinite; }}
    @keyframes roll {{ from {{ transform: translateY(0) }} to {{ transform: translateY({h + 120}px) }} }}
    .blink {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0 }} }}
{style}
    @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
  </style>{body}
</svg>
"""


# ── 1. Cabeçalho: tela de título ─────────────────────────────────────────────
def header() -> str:
    h = 320
    uid = "h"
    abre, fecha = screen_frame(W, h, uid)
    title = "VINICIUS BEZERRA"
    ts = 6
    tx, ty = center_x(title, ts), 112
    sub = "BACK-END DEVELOPER  /  GAMER  /  BUILDER"
    sub_s = 2
    press = "PRESS START"
    ps = 3
    style = f"""
    .glitch-c {{ animation: gc 5s steps(1) infinite; }}
    .glitch-m {{ animation: gm 5s steps(1) infinite; }}
    @keyframes gc {{ 0%,86%,100% {{ transform: translate(3px,0) }} 88% {{ transform: translate(14px,-2px) }} 90% {{ transform: translate(-6px,1px) }} 92% {{ transform: translate(3px,0) }} }}
    @keyframes gm {{ 0%,86%,100% {{ transform: translate(-3px,0) }} 88% {{ transform: translate(-12px,2px) }} 90% {{ transform: translate(8px,-1px) }} 92% {{ transform: translate(-3px,0) }} }}
    .main {{ animation: flick 5s steps(1) infinite; }}
    @keyframes flick {{ 0%,87%,100% {{ opacity: 1 }} 88% {{ opacity: .55 }} 89% {{ opacity: 1 }} 91% {{ opacity: .7 }} }}
    .in {{ animation: in .6s ease-out backwards; }}
    @keyframes in {{ from {{ opacity: 0; transform: translateY(10px) }} to {{ opacity: 1; transform: none }} }}
    .cursor {{ animation: blink .9s steps(1) infinite; }}"""
    ground = []
    # chão em perspectiva (grade que corre em direção à tela)
    for i in range(0, 12):
        y = 252 + i * i * 0.9
        if y > h - 20:
            break
        ground.append(f'<line x1="18" y1="{y:.1f}" x2="{W - 18}" y2="{y:.1f}" />')
    for i in range(-14, 15):
        x2 = W / 2 + i * 70
        ground.append(f'<line x1="{W / 2 + i * 14:.1f}" y1="252" x2="{x2:.1f}" y2="{h}" />')
    body = crt_defs(W, h, uid) + abre + f"""
    {stars(70, W, 240, 7)}
    <g stroke="{MAGENTA}" stroke-opacity="0.28" stroke-width="1.5">{"".join(ground)}</g>
    <rect x="18" y="248" width="{W - 36}" height="4" fill="{MAGENTA}" opacity="0.55"/>

    <path fill="{CYAN}" d="{text_path("1UP", 56, 44, 2)}" class="blink"/>
    <path fill="{INK}" d="{text_path("00002016", 56, 64, 2)}"/>
    <path fill="{MAGENTA}" d="{text_path("HI-SCORE", W - 56 - text_width("HI-SCORE", 2), 44, 2)}"/>
    <path fill="{INK}" d="{text_path("99999999", W - 56 - text_width("99999999", 2), 64, 2)}"/>
    <path fill="{AMBER_DIM}" d="{text_path("VINBEZE.EXE", center_x("VINBEZE.EXE", 2), 44, 2)}"/>

    <g filter="url(#bloom-{uid})">
      <path class="glitch-c" fill="{CYAN}" opacity="0.75" d="{text_path(title, tx, ty, ts)}"/>
      <path class="glitch-m" fill="{MAGENTA}" opacity="0.75" d="{text_path(title, tx, ty, ts)}"/>
      <path class="main" fill="{AMBER}" d="{text_path(title, tx, ty, ts)}"/>
    </g>
    <path class="in" style="animation-delay:.4s" fill="{INK}" d="{text_path(sub, center_x(sub, sub_s), ty + 7 * ts + 26, sub_s)}"/>

    <g class="in" style="animation-delay:.9s">
      <g class="blink"><path fill="{AMBER}" filter="url(#bloom-{uid})" d="{text_path(press, center_x(press, ps), 214, ps)}"/></g>
    </g>
    <rect x="250" y="268" width="460" height="26" fill="{SCREEN}" opacity=".85"/>
    <path fill="{AMBER_DIM}" d="{text_path("(C) 2016-2026  SAO BERNARDO DO CAMPO - SP", center_x("(C) 2016-2026  SAO BERNARDO DO CAMPO - SP", 2), 276, 2)}"/>
""" + fecha
    return svg(W, h, "Vinicius Bezerra — Back-end developer, gamer e builder", style, body)


# ── 2. Ficha do personagem ────────────────────────────────────────────────────
AVATAR = [
    # . vazio  k contorno/órbitas  h cabelo  o osso  g sombra do osso  e olho brilhante
    # c headset  t camiseta  m detalhe  n pescoço
    "......kkkkkkkk......",
    "....kkhhhhhhhhkk....",
    "...khhhhhhhhhhhhk...",
    "..khhhhhhhhhhhhhhk..",
    ".cchhhhhhhhhhhhhhcc.",
    ".ckhhoooooooooohhkc.",
    ".ckgoooooooooooogkc.",
    ".ckgkkkkooookkkkgkc.",
    ".ckokkekooookekkokc.",
    ".ckookkooooookkookc.",
    ".ckgoooookkooooogkc.",
    "..kookkkkkkkkkkookc.",
    "...kokokokokokookcc.",
    "....kkgoooooogkk....",
    "...kttttknnkttttk...",
    "..kttttttttttttttk..",
    ".kttmttttttttttmttk.",
    ".kttmmttttttttmmttk.",
    ".kttttttttttttttttk.",
    ".kkkkkkkkkkkkkkkkkk.",
]
AVATAR_COLORS = {
    "k": "#0a0b12", "h": "#3a2a1e", "o": "#ece6d6", "g": "#b8b0a0", "e": CYAN,
    "n": "#c99272", "c": CYAN, "t": "#2d3a6b", "m": MAGENTA,
}

SKILLS = [
    ("JAVA", 18, AMBER),
    ("C# / .NET", 17, AMBER),
    ("GO", 16, CYAN),
    ("PYTHON", 14, CYAN),
    ("TYPESCRIPT", 13, GREEN),
    ("RUST", 8, MAGENTA),
]


def character() -> str:
    h = 470
    uid = "c"
    abre, fecha = screen_frame(W, h, uid)
    style = """
    .bob { animation: bob 1.6s steps(2) infinite; }
    @keyframes bob { 50% { transform: translateY(-6px) } }
    .eyes { animation: eyes 4s steps(1) infinite; }
    @keyframes eyes { 0%, 100% { fill: #4ff0ff } 46% { fill: #ff4f8b } 50% { fill: #4ff0ff } 52% { fill: #ff4f8b } 54% { fill: #4ff0ff } }
    .shadow { animation: shadow 1.6s steps(2) infinite; transform-origin: 170px 360px; }
    @keyframes shadow { 50% { transform: scaleX(.85) } }"""
    parts = [crt_defs(W, h, uid), abre]

    # Painel esquerdo: retrato
    parts.append(f'<rect x="56" y="56" width="228" height="358" fill="none" stroke="{AMBER}" stroke-width="4"/>')
    parts.append(f'<rect x="64" y="64" width="212" height="342" fill="none" stroke="{AMBER_DIM}" stroke-width="2"/>')
    parts.append(f'<path fill="{AMBER}" d="{text_path("PLAYER 1", 170 - text_width("PLAYER 1", 2) / 2, 82, 2)}"/>')
    parts.append(f'<ellipse class="shadow" cx="170" cy="360" rx="70" ry="7" fill="#000" opacity=".5"/>')
    ax, ay, asc = 70, 140, 10
    avatar = "".join(
        f'<path{" class=\"eyes\" filter=\"url(#bloom-" + uid + ")\"" if ch == "e" else ""} fill="{col}" '
        f'd="{sprite_path(AVATAR, ax, ay, asc, ch)}"/>' for ch, col in AVATAR_COLORS.items()
    )
    parts.append(f'<g class="bob">{avatar}</g>')
    parts.append(f'<path fill="{INK}" d="{text_path("LV 10", 170 - text_width("LV 10", 3) / 2, 378, 3)}"/>')

    # Painel direito: atributos
    x0 = 330
    def row(label: str, value: str, y: int, color: str = INK) -> None:
        parts.append(f'<path fill="{AMBER_DIM}" d="{text_path(label, x0, y, 2)}"/>')
        parts.append(f'<path fill="{color}" d="{text_path(value, x0 + 130, y, 2)}"/>')

    parts.append(f'<path fill="{AMBER}" filter="url(#bloom-{uid})" d="{text_path("STATUS", x0, 60, 3)}"/>')
    parts.append(f'<rect x="{x0}" y="90" width="574" height="2" fill="{AMBER_DIM}"/>')
    row("CLASS", "BACK-END ENGINEER", 106)
    row("GUILD", "JAVA / .NET / GO", 128)
    row("BASE", "ARCH LINUX (BTW)", 150, CYAN)
    row("XP", "10 YEARS OF CODE", 172, GREEN)

    # HP/MP decorativos
    parts.append(f'<path fill="{MAGENTA}" d="{text_path("♥♥♥♥♥", x0 + 400, 106, 2)}"/>')
    parts.append(f'<path fill="{CYAN}" d="{text_path("★★★★", x0 + 400, 128, 2)}"/>')

    parts.append(f'<path fill="{AMBER}" filter="url(#bloom-{uid})" d="{text_path("SKILLS", x0, 210, 3)}"/>')
    parts.append(f'<rect x="{x0}" y="240" width="574" height="2" fill="{AMBER_DIM}"/>')
    seg_w, seg_gap, n_seg = 16, 4, 20
    for i, (name, lvl, color) in enumerate(SKILLS):
        y = 258 + i * 26
        parts.append(f'<path fill="{INK}" d="{text_path(name, x0, y + 1, 2)}"/>')
        bx = x0 + 150
        for s in range(n_seg):
            if s < lvl:
                delay = 0.6 + i * 0.25 + s * 0.05
                # Nasce aceso; o <animate> só o mantém apagado até a sua vez (sem fill=freeze).
                parts.append(
                    f'<rect x="{bx + s * (seg_w + seg_gap)}" y="{y}" width="{seg_w}" height="14" fill="{color}">'
                    f'<animate attributeName="opacity" values=".12;.12" dur="{delay:.2f}s" begin="0s"/></rect>'
                )
            else:
                parts.append(
                    f'<rect x="{bx + s * (seg_w + seg_gap)}" y="{y}" width="{seg_w}" height="14" fill="{DIM}" opacity=".35"/>'
                )
    parts.append(
        f'<path class="blink" fill="{MAGENTA}" d="{text_path("NEW!", x0 + 150 + 8 * 20 + 6, 258 + 5 * 26 + 1, 2)}"/>'
    )
    parts.append(fecha)
    return svg(W, h, "Ficha do personagem: back-end engineer, nível 10", style, "".join(parts))


# ── 3. Rodapé: continue? ──────────────────────────────────────────────────────
SHIP = [
    "....cc..........",
    "....ccc.........",
    "..kkaaakk.......",
    ".kaaaaaaaakk....",
    "kaawwaaaaaaaakk.",
    "kaawwaaaaaaaaaam",
    ".kaaaaaaaakk....",
    "..kkaaakk.......",
    "....ccc.........",
    "....cc..........",
]
SHIP_COLORS = {"k": "#0a0b12", "a": AMBER, "w": CYAN, "c": MAGENTA, "m": INK}


def footer() -> str:
    h = 200
    uid = "f"
    abre, fecha = screen_frame(W, h, uid)
    style = f"""
    .far {{ animation: scroll 24s linear infinite; }}
    .near {{ animation: scroll 9s linear infinite; }}
    @keyframes scroll {{ from {{ transform: translateX(0) }} to {{ transform: translateX(-{W}px) }} }}
    .ship {{ animation: fly 3s ease-in-out infinite alternate; }}
    @keyframes fly {{ from {{ transform: translate(0,-8px) }} to {{ transform: translate(26px,8px) }} }}
    .flame {{ animation: blink .18s steps(1) infinite; }}
    .shot {{ animation: shot 1.4s linear infinite; }}
    @keyframes shot {{ from {{ transform: translateX(0); opacity: 1 }} 80% {{ opacity: 1 }} to {{ transform: translateX(560px); opacity: 0 }} }}
    .n {{ opacity: 0; animation: n 10s steps(1) infinite; }}
    @keyframes n {{ 0% {{ opacity: 1 }} 10% {{ opacity: 0 }} }}"""
    rnd = random.Random(3)
    def layer(cls: str, n: int, size: int, color: str, op: float) -> str:
        rects = []
        for _ in range(n):
            x = rnd.randint(0, W)
            y = rnd.randint(30, h - 30)
            for dx in (0, W):  # duplicado para loop contínuo
                rects.append(f'<rect x="{x + dx}" y="{y}" width="{size * 3 if cls == "near" else size}" height="{size}" fill="{color}"/>')
        return f'<g class="{cls}" opacity="{op}">{"".join(rects)}</g>'

    ship = "".join(f'<path fill="{c}" d="{sprite_path(SHIP, 110, 74, 5, ch)}"/>' for ch, c in SHIP_COLORS.items())
    flame = f'<rect class="flame" x="96" y="96" width="12" height="10" fill="{MAGENTA}"/>'
    shot = f'<rect class="shot" x="196" y="99" width="20" height="4" fill="{CYAN}"/>'
    msg = "THANKS FOR PLAYING"
    cont = "CONTINUE?"
    cx = 560
    digits = "".join(
        f'<path class="n" style="animation-delay:{i}s" fill="{MAGENTA}" d="{text_path(str(9 - i), cx + text_width(cont, 4) + 24, 108, 4)}"/>'
        for i in range(10)
    )
    body = crt_defs(W, h, uid) + abre + f"""
    {layer("far", 40, 2, INK, .45)}
    {layer("near", 14, 3, CYAN, .5)}
    <g class="ship">{flame}{ship}{shot}</g>
    <path fill="{AMBER}" filter="url(#bloom-{uid})" d="{text_path(msg, cx - 30, 62, 3)}"/>
    <path fill="{INK}" d="{text_path(cont, cx, 108, 4)}"/>
    {digits}
    <path fill="{AMBER_DIM}" d="{text_path("INSERT COIN TO FOLLOW", cx - 30, 154, 2)}"/>
""" + fecha
    return svg(W, h, "Thanks for playing — continue?", style, body)


(OUT / "header.svg").write_text(header(), encoding="utf-8")
(OUT / "character.svg").write_text(character(), encoding="utf-8")
(OUT / "footer.svg").write_text(footer(), encoding="utf-8")
print("ok:", ", ".join(p.name for p in sorted(OUT.glob("*.svg"))))
