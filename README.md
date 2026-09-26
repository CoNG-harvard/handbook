# CoNG Handbook

Source for the CoNG lab's hardware platform setup manuals, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published with GitHub Pages at <https://cong-harvard.github.io/handbook/>.

## Read the setup manual

The handbook helps readers with little robotics experience gather equipment, identify parts, assemble and connect each platform, and complete an operator-led hardware readiness check.

- [Before you begin](docs/getting-started/index.md), [shared equipment](docs/getting-started/hardware.md), and [workstation preparation](docs/getting-started/computer.md)
- [VLA Pipeline](docs/vla-pipeline/index.md): two xArm robots, wrist/scene cameras, and Quest headsets
- [Self Improvement Learning](docs/unidog-nav/index.md): Unitree Go2, D1 arm, front D435i, D435 wrist camera, and onboard computer
- [ABC Box](docs/abc-box/index.md): followers, leaders, and three D405 cameras; shared-workstation connections require supplier confirmation

All three projects share one workstation with **one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**. Equipment references distinguish observed inventory from parts still requiring confirmation. No hardware acceptance test was performed during the documentation update.

## Preview locally

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000, reloads on save
```

## Layout

| Path | What it is |
|---|---|
| `docs/index.md` | Project directory with links to shared setup |
| `docs/<project>/` | Hardware guides and labeled photos in `assets/` |
| `archive/previous-guide/` | Previous text retained for maintainers, outside the published site |
| `mkdocs.yml` | Theme, navigation, and link validation |
| `overrides/partials/tabs.html` | Shared desktop navigation and compact mobile menu |
| `docs/stylesheets/handbook.css` | Typography, project cards, and responsive layout |
| `.github/workflows/pages.yml` | Builds the site and publishes it to GitHub Pages |

## Adding a project

1. Create `docs/<project>/index.md` plus any further pages, using relative links.
2. Add a top-level entry for it under `nav:` in `mkdocs.yml`.
3. Add a project card to `docs/index.md`, following the existing markup.
4. Replace private details (LAN IPs, device serials, `/home/<user>/` paths) with placeholders such as `<ROBOT_IP>`.
5. Check that `mkdocs build --strict` passes. It fails on broken links.

## Deployment

Every push to `main` runs `.github/workflows/pages.yml`, which runs `mkdocs build --strict` and publishes `site/` to GitHub Pages. A failed build (for example a broken link) leaves the previous version live. Build logs are in the repo's **Actions** tab.

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

## Writing setup instructions

Keep the published site focused on equipment, quantities, mounting, power/data connections, camera positions, device labels, calibration requirements, stop controls, and readiness. Explain unfamiliar hardware terms and state the expected result of each check. Use manufacturer instructions for exact mounting loads, fasteners, wiring, and electrical requirements rather than inventing specifications.

Software installation, environments, launch commands, model training/inference, datasets, source-transfer recipes, and software-release references do not belong in the published manual. The earlier material is retained in `archive/previous-guide/` for maintainers; do not include that directory in the site build or search index.

Keep actual device serials and network addresses in private station records. Record equipment evidence and unresolved physical requirements in `docs/getting-started/sources.md`. Run `mkdocs build --strict` before review; link and anchor warnings fail that build. Building the site does not validate hardware or external links.

Use real photographs with accurate callouts and captions. If a photograph is unavailable, use an explicit photo placeholder. Never substitute generated equipment photos.

## Website style conventions

Keep visual rules in `docs/stylesheets/handbook.css`; avoid page-specific fonts, colors, or inline styles. Use one page title, numbered headings for sequential setup, and unnumbered headings for reference material. Tables, code blocks, notes, and warnings share the global styles; keep warning colors distinct from informational notes.

Wrap images in `figure.handbook-figure` with a plain-text `figcaption` and a `.figure-links` paragraph. Use **View full-size image** and, when available, **Source photograph** or **Source PDF**. Follow the markup in `docs/unidog-nav/index.md`. Preserve each real image's aspect ratio and existing labels.

Project display names are **VLA Pipeline**, **Self Improvement Learning**, and **ABC Box**. Preserve the existing project URL roots.

Keep the same top-level navigation tabs on every page. Navigation remains in the header while scrolling. Desktop links separate shared setup from the projects; narrow screens use a native disclosure menu showing the current section. Both layouts are generated from the same navigation configuration. Each project sidebar begins with **Overview**, followed by equipment/connections and hardware readiness; include platform-specific checks such as D1 readiness where needed.

Hardware inventories use short equipment, quantity, and product/reference tables with selection details below. Link every equipment row to a verified product, supplier catalog, or relevant assembly reference; mark unspecified custom parts without inventing a purchase model. Clearly identify unverified custom parts and pending commissioning procedures. Keep each project's equipment separate and count the shared workstation only once.

The new station photographs use unnumbered vector callouts with camera model names and matching captions. Regenerate the annotated SVGs with `python3 scripts/label_photos.py`; the source JPEGs remain unchanged. Label only identifiable visible equipment, and do not infer rig A/B identities from position.

## Maintaining the setup aids

Keep unknown connections explicitly marked; do not infer port maps from photographs. Connection maps are HTML/CSS so they remain readable on phones and in both themes. Shared setup covers only the shared equipment; project overview pages hold the full identification photographs. End each readiness page with the station record and a return to its own project.

The station record is a two-sheet print layout. It contains no storage or upload mechanism; completed records stay private. Checklists are static and intended for printing.

The labeled xArm and ABC SVGs embed checked-in 1800-pixel previews. Source JPEGs stay unchanged. To regenerate the previews on macOS, then rebuild vector labels:

```bash
sips -Z 1800 -s format jpeg -s formatOptions 82 docs/vla-pipeline/assets/xarm-station.jpg --out docs/vla-pipeline/assets/xarm-station-preview.jpg
sips -Z 1800 -s format jpeg -s formatOptions 82 docs/abc-box/assets/abc-box-station.jpg --out docs/abc-box/assets/abc-box-station-preview.jpg
python3 scripts/label_photos.py
```

Verify mobile tables scroll without clipping, connection maps stack, and the station record prints with its two sections on separate sheets. Keep the source images and vector labels when optimizing image delivery.
