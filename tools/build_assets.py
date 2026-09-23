"""Build the profile's self-contained SVG artwork. No external dependencies."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PALETTES = {
    "dark": {"ink": "#E7E2D9", "paper": "#0D1117", "accent": "#B49B78", "muted": "#7D817F"},
    "light": {"ink": "#33332F", "paper": "#FFFFFF", "accent": "#8D7454", "muted": "#777B76"},
}


def hero(theme):
    p = PALETTES[theme]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-labelledby="title desc">
  <title id="title">Medusa — a Greek cameo</title>
  <desc id="desc">A sculpted profile framed by five curling serpents, in ivory and bronze. The outer serpents move gently.</desc>
  <g fill="none" stroke="{p['accent']}" stroke-width=".8" opacity=".38">
    <circle cx="320" cy="169" r="125"/>
    <path d="M133 169h34m306 0h34"/>
  </g>
  <g fill="none" stroke="{p['ink']}" stroke-linecap="round" stroke-linejoin="round">
    <!-- The silhouette stays still; only two outer snakes gently stir. -->
    <g class="motion" stroke-width="7">
      <animateTransform attributeName="transform" type="rotate" values="-2.5 288 216;2.5 288 216;-2.5 288 216" dur="9s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M288 216c-31 4-64-16-66-45-2-20 12-28 21-19 13 13-7 27-19 14-17-18-2-40 12-57 12-15 7-31-7-32"/>
      <path d="M230 77c-7-8-19-7-22-1 4 8 15 10 22 1Z" fill="{p['ink']}" stroke-width="2"/>
      <circle cx="215" cy="76" r="1.4" fill="{p['paper']}" stroke="none"/>
    </g>
    <g class="motion" stroke-width="7">
      <animateTransform attributeName="transform" type="rotate" values="-2.5 319 122;2.5 319 122;-2.5 319 122" dur="12s" begin="-4s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M319 122c13-31 40-45 66-36 20 7 29 31 17 42-10 9-24 2-21-9 3-10 17-12 27-2 17 17 12 39-7 38"/>
      <path d="M401 155c-3-8-14-12-20-6 1 9 13 12 20 6Z" fill="{p['ink']}" stroke-width="2"/>
      <circle cx="387" cy="150" r="1.4" fill="{p['paper']}" stroke="none"/>
    </g>
    <g stroke-width="8">
      <path d="M278 186c-26-25-28-52-10-73 13-15 33-16 43-33 9-17-3-31-16-28-13 3-12 18-2 21 9 3 19-6 25-13"/>
      <path d="M318 60c-1-9 7-17 15-14 3 9-6 17-15 14Z" fill="{p['ink']}" stroke-width="2"/>
      <circle cx="329" cy="51" r="1.4" fill="{p['paper']}" stroke="none"/>
      <path d="M299 133c-2-26-18-44-35-42-19 2-21 22-10 28 9 4 15-1 17-7"/>
      <path d="M271 112c-1-8 7-15 14-11 1 8-6 14-14 11Z" fill="{p['ink']}" stroke-width="2"/>
      <circle cx="281" cy="105" r="1.3" fill="{p['paper']}" stroke="none"/>
      <path d="M291 178c-24 13-47 30-41 52 4 17 25 19 30 8 5-11-7-20-15-14"/>
      <path d="M265 224c-8-5-17 0-17 8 7 5 16 1 17-8Z" fill="{p['ink']}" stroke-width="2"/>
      <circle cx="253" cy="230" r="1.3" fill="{p['paper']}" stroke="none"/>
    </g>
  </g>
  <!-- Classical profile: continuous forehead/nose, quiet eye, long neck. -->
  <path d="M292 122c16-19 45-21 62-5 12 11 10 26 13 39l17 29c2 4-3 6-12 6l-2 10 6 4-7 6c3 13-7 22-21 19l-8-2c-2 17 5 29 21 42h-76c20-19 28-34 25-52-3-18-17-22-26-42-9-20-7-39 8-54Z" fill="{p['ink']}"/>
  <path d="M291 125c17-19 43-20 58-8-13-2-24 3-31 13-8 11-9 28-15 38-5-12-13-14-20-9-2-14 0-25 8-34Z" fill="{p['paper']}"/>
  <g fill="none" stroke="{p['paper']}" stroke-linecap="round" stroke-linejoin="round">
    <path d="M343 157q9-5 17 0m-17 6q8 5 16-1" stroke-width="2"/>
    <path d="m351 164 3 2m9 42 7-1" stroke-width="1.6"/>
    <path d="M293 169c-7-9-15-3-11 8 2 7 7 10 11 7m-5-11 1 6" stroke-width="2"/>
    <path d="M309 192c4 13 14 23 28 28m-10 16c-1 11-4 20-10 27" stroke-width="1.5" opacity=".7"/>
  </g>
  <g fill="none" stroke="{p['accent']}" stroke-linecap="round">
    <path d="M296 125c15-19 33-26 52-18" stroke-width="2.5"/>
    <circle cx="289" cy="191" r="4" stroke-width="1.8"/>
  </g>
  <path d="M287 278h74" stroke="{p['accent']}" stroke-width="1"/>
  <text x="323" y="323" fill="{p['muted']}" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="12" letter-spacing="6">MEDUSA</text>
</svg>
'''
    return svg


ICONS = {
    "mokka": ('Mokka — architecture', '<path d="M7 26V12l9-6 9 6v14M4 26h24M11 25V15h10v10M16 15v10"/>'),
    "klar": ('Klarbescheid — clarity', '<path d="M8 4h11l5 5v19H8ZM19 4v6h5M12 15h8m-8 5 3 3 6-7"/>'),
    "mask": ('Datenmaske — privacy', '<path d="M16 4 26 8v7c0 6-4 10-10 13C10 25 6 21 6 15V8Z"/><path d="M11 13h10v7H11Z" fill="INK" stroke="none"/>'),
    "studio": ('Studio — coordination', '<rect x="5" y="5" width="8" height="8" rx="1"/><rect x="19" y="5" width="8" height="8" rx="1"/><rect x="5" y="19" width="8" height="8" rx="1"/><rect x="19" y="19" width="8" height="8" rx="1"/>'),
}


def icon(name, theme):
    ink = PALETTES[theme]["ink"]
    title, drawing = ICONS[name]
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><title>{title}</title><g fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{drawing.replace("INK", ink)}</g></svg>\n'


if __name__ == "__main__":
    for theme in PALETTES:
        (ASSETS / f"hero-{theme}.svg").write_text(hero(theme), encoding="utf-8", newline="\n")
        # Select static artwork in README <picture>, where media queries are
        # evaluated by the page rather than the isolated SVG image document.
        static = re.sub(r'\s*<animateTransform[^>]*/>', '', hero(theme))
        static = static.replace('The outer serpents move gently.', 'A still illustration for reduced motion.')
        (ASSETS / f"hero-still-{theme}.svg").write_text(static, encoding="utf-8", newline="\n")
        for name in ICONS:
            (ASSETS / f"px-{name}-{theme}.svg").write_text(icon(name, theme), encoding="utf-8", newline="\n")
    (ASSETS / "hero.svg").write_text(hero("dark"), encoding="utf-8", newline="\n")
    for name in ICONS:
        (ASSETS / f"px-{name}.svg").write_text(icon(name, "dark"), encoding="utf-8", newline="\n")
    (ASSETS / "divider.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="768" height="24" viewBox="0 0 768 24"><path d="M0 12h358m52 0h358" stroke="#8D8477" stroke-opacity=".3"/><path d="m380 12 4-4 4 4-4 4Z" fill="#A58D6C"/></svg>\n', encoding="utf-8", newline="\n")
