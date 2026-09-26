"""Build vector callouts over the original, unmodified lab photographs.

Coordinates use a 1000-unit-wide viewBox with the source aspect ratio. Regenerate from the repository root with
python3 scripts/label_photos.py. Keep source JPEGs for the unannotated download.
"""
from base64 import b64encode
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def annotate(folder, stem, title, description, labels, extension='jpg', height=750):
    source = ROOT / 'docs' / folder / 'assets' / f'{stem}.{extension}'
    photo = b64encode(source.read_bytes()).decode('ascii')
    mime = 'image/png' if extension == 'png' else 'image/jpeg'
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" '
        f'viewBox="0 0 1000 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        '<!-- Original image embedded unchanged; annotations are separate vectors. -->',
        f'<image width="1000" height="{height}" href="data:{mime};base64,{photo}"/>',
    ]
    # White halos keep the leaders visible against both dark and light equipment.
    for text, x, y, width, targets in labels:
        for start_x, start_y, end_x, end_y in targets:
            path = f'M{start_x} {start_y} L{end_x} {end_y}'
            parts += [
                f'<path d="{path}" fill="none" stroke="white" stroke-width="6"/>',
                f'<path d="{path}" fill="none" stroke="#173958" stroke-width="2.5"/>',
                f'<circle cx="{end_x}" cy="{end_y}" r="5" fill="#173958" stroke="white" stroke-width="2"/>',
            ]
    # Draw all text above the leader lines, so lines never obscure labels.
    for text, x, y, width, targets in labels:
        parts += [
            f'<rect x="{x}" y="{y}" width="{width}" height="42" rx="7" '
            'fill="#102f4e" stroke="white" stroke-width="2"/>',
            f'<text x="{x+width/2}" y="{y+28}" text-anchor="middle" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="600" fill="white">{escape(text)}</text>',
        ]
    parts.append('</svg>')
    source.with_name(f'{stem}-labeled.svg').write_text('\n'.join(parts)+'\n')


annotate('vla-pipeline', 'xarm-station', 'VLA Pipeline — labeled xArm station',
         'The original lab photograph with callouts: both xArm robots; the visible foreground gripper; '
         'all three D435 scene cameras on stands; the two D405 wrist-mounted cameras. Labels do not assign rig A/B identities.', [
    ('xArm robots (2)', 28, 295, 222, [(90,337,112,410),(210,337,335,570)]),
    ('Gripper', 625, 505, 153, [(625,547,547,641)]),
    ('RealSense D435 (3)', 480, 55, 320, [(490,97,244,208),(585,97,465,183),(735,97,822,135)]),
    ('RealSense D405 (2)', 45, 495, 320, [(240,495,249,444),(365,516,550,518)]),
])
annotate('abc-box', 'abc-box-station', 'ABC Box — labeled lab station',
         'The original lab photograph with callouts: both robot arms; the two D405 wrist cameras; '
         'the overhead D405 camera; the camera support frame. Leader arms and stop controls are not identified in this view.', [
    ('Robot arms (2)', 475, 475, 224, [(485,517,300,603),(655,517,621,603)]),
    ('RealSense D405 (2)', 500, 248, 256, [(515,290,373,403),(710,290,687,378)]),
    ('RealSense D405 (1)', 184, 35, 256, [(184,56,106,32)]),
    ('Camera frame', 35, 305, 221, [(230,347,309,415)]),
])

annotate('unidog-nav', 'platform', 'Self Improvement Learning — Go2 and D1 cameras',
         'Original platform image with existing Go2, D1 arm, and front D435i labels, plus a D435 wrist camera label beside the gripper.', [
    ('D435 wrist camera', 30, 490, 295, [(165,490,160,410)]),
], extension='png', height=1030/1.8)
