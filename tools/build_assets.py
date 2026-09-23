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
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="330" viewBox="0 0 640 330" role="img" aria-labelledby="title desc">
  <title id="title">Medusa — a Greek cameo</title>
  <desc id="desc">A forward-facing Medusa with a calm, direct gaze, in ivory and bronze. Her eyes blink and the serpents move gently.</desc>
  <g fill="none" stroke="{p['accent']}" stroke-width=".8" opacity=".38">
    <circle cx="320" cy="169" r="125"/>
    <path d="M133 169h34m306 0h34"/>
  </g>
  <g fill="none" stroke="{p['ink']}" stroke-linecap="round" stroke-linejoin="round">
    <!-- Serpents face outward toward the viewer and sway from their roots. -->
    <g class="motion" stroke-width="7">
      <animateTransform attributeName="transform" type="rotate" values="-2.5 288 216;2.5 288 216;-2.5 288 216" dur="9s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M288 216c-31 4-64-16-66-45-2-20 12-28 21-19 13 13-7 27-19 14-17-18-2-40 12-57 12-15 2-27-16-26"/>
      <path d="M220 85c-10-4-14-13-8-18q8-5 16 0c6 5 2 14-8 18Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="215" cy="73" r="1.5"/><circle cx="225" cy="73" r="1.5"/></g>
    </g>
    <g class="motion" stroke-width="7">
      <animateTransform attributeName="transform" type="rotate" values="-2.5 319 122;2.5 319 122;-2.5 319 122" dur="12s" begin="-4s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M319 122c13-31 40-45 66-36 20 7 29 31 17 42-10 9-24 2-21-9 3-10 17-12 27-2 17 17 12 39-7 38"/>
      <path d="M395 160c-10-4-14-13-8-18q8-5 16 0c6 5 2 14-8 18Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="390" cy="148" r="1.5"/><circle cx="400" cy="148" r="1.5"/></g>
    </g>
    <g stroke-width="8">
      <animateTransform attributeName="transform" type="rotate" values="-1 296 176;1 296 176;-1 296 176" dur="15s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M278 186c-26-25-28-52-10-73 13-15 33-16 43-33 9-17-3-31-16-28-13 3-12 18-2 21 9 3 19-6 25-13"/>
      <path d="M325 63c-10-4-14-13-8-18q8-5 16 0c6 5 2 14-8 18Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="320" cy="51" r="1.5"/><circle cx="330" cy="51" r="1.5"/></g>
      <path d="M299 133c-2-26-18-44-35-42-19 2-21 22-10 28 9 4 15-1 17-7"/>
      <path d="M278 115c-8-3-12-11-7-15q7-4 14 0c5 4 1 12-7 15Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="274" cy="104" r="1.3"/><circle cx="282" cy="104" r="1.3"/></g>
      <path d="M291 178c-24 13-47 30-41 52 4 17 25 19 30 8 5-11-7-20-15-14"/>
      <path d="M256 237c-8-3-12-11-7-15q7-4 14 0c5 4 1 12-7 15Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="252" cy="226" r="1.3"/><circle cx="260" cy="226" r="1.3"/></g>
    </g>
    <g stroke-width="7">
      <animateTransform attributeName="transform" type="rotate" values="1.5 349 178;-1.5 349 178;1.5 349 178" dur="10s" repeatCount="indefinite" calcMode="spline" keyTimes="0;.5;1" keySplines=".45 0 .55 1;.45 0 .55 1"/>
      <path d="M349 178c24 13 47 30 41 52-4 17-25 19-30 8-5-11 7-20 15-14"/>
      <path d="M383 237c-8-3-12-11-7-15q7-4 14 0c5 4 1 12-7 15Z" fill="{p['ink']}" stroke-width="2"/>
      <g fill="{p['paper']}" stroke="none"><circle cx="379" cy="226" r="1.3"/><circle cx="387" cy="226" r="1.3"/></g>
    </g>
  </g>
  <!-- Frontal cameo: balanced features, direct gaze and a quiet expression. -->
  <path d="M300 215h40c-4 24 0 39 22 55h-84c22-16 26-31 22-55Z" fill="{p['ink']}"/>
  <path d="M280 132c1-20 19-31 40-26 21-5 39 6 40 26 4 20 3 43-4 62-7 18-24 35-36 38-12-3-29-20-36-38-7-19-8-42-4-62Z" fill="{p['ink']}"/>
  <path d="M280 139c-1-26 18-38 40-32 22-6 41 6 40 32-10-19-24-22-40-14-16-8-30-5-40 14Z" fill="{p['paper']}"/>
  <g fill="none" stroke="{p['paper']}" stroke-linecap="round" stroke-linejoin="round">
    <path d="M289 151q10-6 21 0m20 0q11-6 21 0" stroke-width="2.2"/>
    <path d="M319 162v23l-4 5q5 4 10 0" stroke-width="1.6"/>
    <path d="M308 205q6-1 12 0 6-1 12 0m-18 5q6 3 12 0" stroke-width="1.5"/>
    <path d="M286 181q3 16 11 23m57-23q-3 16-11 23M301 225q19 15 38 0m-31 13-5 23m29-23 5 23" stroke-width="1.2" opacity=".55"/>
  </g>
  <g transform="translate(320 164)">
    <g id="eyes">
      <animateTransform attributeName="transform" type="scale" values="1 1;1 1;1 .08;1 1;1 1" keyTimes="0;.72;.738;.762;1" dur="7s" repeatCount="indefinite"/>
      <g fill="none" stroke="{p['paper']}" stroke-width="1.7" stroke-linecap="round">
        <path d="M-31 0q11-9 22 0-11 8-22 0Zm40 0q11-9 22 0-11 8-22 0Z"/>
      </g>
      <g fill="{p['paper']}">
        <animateTransform attributeName="transform" type="translate" values="0 0;0 0;1 0;0 0;0 0" keyTimes="0;.35;.45;.55;1" dur="11s" repeatCount="indefinite"/>
        <circle cx="-20" cy="0" r="3.2"/><circle cx="20" cy="0" r="3.2"/>
      </g>
    </g>
  </g>
  <g fill="none" stroke="{p['accent']}" stroke-linecap="round">
    <path d="M288 121q32-26 64 0" stroke-width="2"/>
    <circle cx="279" cy="191" r="4" stroke-width="1.8"/><circle cx="361" cy="191" r="4" stroke-width="1.8"/>
  </g>
  <path d="M283 278h74" stroke="{p['accent']}" stroke-width="1"/>
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
        static = static.replace('Her eyes blink and the serpents move gently.', 'A still illustration for reduced motion.')
        (ASSETS / f"hero-still-{theme}.svg").write_text(static, encoding="utf-8", newline="\n")
        for name in ICONS:
            (ASSETS / f"px-{name}-{theme}.svg").write_text(icon(name, theme), encoding="utf-8", newline="\n")
    (ASSETS / "hero.svg").write_text(hero("dark"), encoding="utf-8", newline="\n")
    for name in ICONS:
        (ASSETS / f"px-{name}.svg").write_text(icon(name, "dark"), encoding="utf-8", newline="\n")
    (ASSETS / "divider.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="768" height="24" viewBox="0 0 768 24"><path d="M0 12h358m52 0h358" stroke="#8D8477" stroke-opacity=".3"/><path d="m380 12 4-4 4 4-4 4Z" fill="#A58D6C"/></svg>\n', encoding="utf-8", newline="\n")
