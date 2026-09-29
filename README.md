# CoNG Handbook

Source for the CoNG lab's hardware platform and basic software setup manuals, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published with GitHub Pages at <https://cong-harvard.github.io/handbook/>.

## Read the setup manual

The handbook helps readers with little robotics experience gather equipment, identify parts, assemble and connect each platform, install basic device software, and complete an operator-led hardware readiness check.

- [Before you begin](docs/getting-started/index.md), [shared equipment](docs/getting-started/hardware.md), [workstation preparation](docs/getting-started/computer.md), [basic software](docs/getting-started/software.md), [safety](docs/getting-started/safety.md), and a [glossary](docs/getting-started/glossary.md)
- [VLA Pipeline](docs/vla-pipeline/index.md): two xArm robots, wrist/scene cameras, and Quest headsets
- [Self Improvement Learning](docs/unidog-nav/index.md): Unitree Go2, D1 arm, front D435i, D435 wrist camera, and onboard computer
- [ABC Box](docs/abc-box/index.md): followers, leaders, and three D405 cameras; shared-workstation connections require supplier confirmation

- [TurtleBot3 Burger](docs/turtlebot3/index.md): wheeled robots, LiDAR, a matching ROS environment, and optional OptiTrack tracking

VLA Pipeline, Self Improvement Learning, and ABC Box share one workstation with **one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**. TurtleBot3 needs an operator environment matching the robot; compatibility with the shared Ubuntu 24.04 installation is not established. Equipment references distinguish observed inventory from parts still requiring confirmation. No hardware acceptance test was performed during the documentation update.

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
| `docs/<project>/` | Hardware and basic software guides, plus labeled photos in `assets/` |
| `archive/previous-guide/` | Previous text retained for maintainers, outside the published site |
| `mkdocs.yml` | Theme, navigation, and link validation |
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

Keep the published site focused on equipment, quantities, mounting, power/data connections, camera positions, device labels, calibration requirements, stop controls, and readiness. Define hardware terms in `docs/getting-started/glossary.md` and put station-wide rules in `docs/getting-started/safety.md`. State the expected result of each check.

Write as a manual, not an audit: state facts plainly and put every unresolved item in the **Open items** section of `docs/getting-started/sources.md` rather than hedging inside equipment rows. Provenance (who confirmed what, when, and what a photograph does or does not show) belongs in `validation/`, not in `docs/`. Use manufacturer instructions for exact mounting loads, fasteners, wiring, and electrical requirements rather than inventing specifications.

Include basic software that makes the hardware usable: operating-system preparation, supported drivers, manufacturer tools and SDKs, camera viewers, network/USB connections, and device checks with expected results. Keep installation instructions tied to official vendor guidance and identify the computer where each step runs. Research code, model training/inference, research datasets, experiment workflows, private source-transfer recipes, and research-release instructions do not belong in the published manual. The earlier material is retained in `archive/previous-guide/` for maintainers; do not include that directory in the site build or search index.

Keep actual device serials and network addresses in private station records. Record equipment evidence and unresolved physical requirements in `docs/getting-started/sources.md`. Run `mkdocs build --strict` before review; link and anchor warnings fail that build. Building the site does not validate hardware or external links.

Use real photographs with accurate callouts and captions. If a photograph is unavailable, use an explicit photo placeholder. Never substitute generated equipment photos.

## Website style conventions

Keep visual rules in `docs/stylesheets/handbook.css`; avoid page-specific fonts, colors, or inline styles. Use one page title, numbered headings for sequential setup, and unnumbered headings for reference material. Tables, code blocks, notes, and warnings share the global styles; keep warning colors distinct from informational notes.

Wrap images in `figure.handbook-figure` with a plain-text `figcaption` and a `.figure-links` paragraph. Use **View full-size image** and, when available, **Source photograph** or **Source PDF**. Follow the markup in `docs/unidog-nav/index.md`. Preserve each real image's aspect ratio and existing labels.

Project display names are **VLA Pipeline**, **Self Improvement Learning**, and **ABC Box**. Preserve the existing project URL roots.

Keep the full handbook navigation in the left sidebar on every page, including the project directory. Group shared setup and all projects in the same order and highlight the current page. On narrow screens, the header menu opens the same navigation in a drawer. Use MkDocs Material’s section and expansion features with the single `nav` configuration; do not restrict the sidebar to the active project. Each project sidebar begins with **Overview**, followed by equipment/connections, basic software, and hardware readiness; include platform-specific pages such as the D1 mounting page where needed. Use straight apostrophes; use the word "workstation" (not desktop or desk computer) for the shared computer.

Every hardware page follows the same skeleton: **1. Equipment** (tables with the columns Equipment · Quantity · Product or reference, digits-only quantities such as `4 (2 per gripper)`, then **Notes on selection**), **2. Connection map**, **3. Assemble and connect**, **4. Record identities**. Every readiness page follows **1. Inspect before power-on · 2. Check the camera views · 3. Confirm stops and clearance · 4. Record the handover**. Overview pages open with a **What you need** box listing core equipment and open items. Link every equipment row to a verified product, supplier catalog, or relevant assembly reference; mark unspecified custom parts without inventing a purchase model. Clearly identify unverified custom parts and pending commissioning procedures. Keep each project's equipment separate and count the shared workstation only once.

The new station photographs use unnumbered vector callouts with camera model names and matching captions. Regenerate the annotated SVGs with `python3 scripts/label_photos.py`; the source JPEGs remain unchanged. Label only identifiable visible equipment, and do not infer rig A/B identities from position.

## Maintaining the setup aids

Keep unknown connections explicitly marked; do not infer port maps from photographs. Connection maps are HTML/CSS so they remain readable on phones and in both themes. Shared setup covers only the shared equipment; project overview pages hold the full identification photographs. End each readiness page with troubleshooting help and a return to its own project.

Checklists are static and intended for printing. Readers keep their own setup notes privately.

The labeled xArm and ABC SVGs embed checked-in 1800-pixel previews. Source JPEGs stay unchanged. To regenerate the previews on macOS, then rebuild vector labels:

```bash
sips -Z 1800 -s format jpeg -s formatOptions 82 docs/vla-pipeline/assets/xarm-station.jpg --out docs/vla-pipeline/assets/xarm-station-preview.jpg
sips -Z 1800 -s format jpeg -s formatOptions 82 docs/abc-box/assets/abc-box-station.jpg --out docs/abc-box/assets/abc-box-station-preview.jpg
python3 scripts/label_photos.py
```

Verify mobile tables scroll without clipping, connection maps stack, and pages remain readable when printed. Keep the source images and vector labels when optimizing image delivery.
