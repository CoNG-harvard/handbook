# CoNG Handbook

Source for the CoNG lab's project manuals, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published with GitHub Pages at <https://cong-harvard.github.io/handbook/>.

## Read the setup manual

The handbook is written for people preparing new Linux workstations with little prior robotics context.

- [Before you begin](docs/getting-started/index.md), [hardware checklist](docs/getting-started/hardware.md), and [computer preparation](docs/getting-started/computer.md)
- Both projects share **one workstation with one RTX PRO 6000 Blackwell Workstation Edition, 96 GB**. Each project has its own robot hardware list.
- [VLA Pipeline two-arm station](docs/vla-pipeline/index.md): hardware → installation → headset recording → model inference
- [Self Improvement Learning robot dog](docs/unidog-nav/index.md): installation → mock check → camera bridge → supervised movement
- [Source handoff and verification limits](docs/getting-started/sources.md)

The September 2026 edition was checked against the lab working trees. It is not a claim of a completed fresh-machine installation or hardware acceptance test. Several custom sources, environments, and model assets require a lab handoff.

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
| `docs/<project>/` | One folder per project; images go in `docs/<project>/assets/` |
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

State which computer and folder each command uses, define unfamiliar terms, and give an expected result before the next step. Keep complete installation steps ahead of advanced experiments. Identify commands that connect to hardware or move a robot, including reset commands. Use source-verified CLI arguments and configuration layouts; distinguish observed versions from a tested dependency lock.

Keep machine-specific values private. Record source provenance and unresolved installation dependencies in `docs/getting-started/sources.md`. Run `mkdocs build --strict` before review; link and anchor warnings are configured to fail that build. Building the site does not test the robot software or external web links.

Use real photographs for project equipment, with captions identifying the setup shown. If a photograph is unavailable, use an explicit photo placeholder. Do not substitute generated or schematic pictures for equipment photos.

## Website style conventions

Keep visual rules in `docs/stylesheets/handbook.css`; avoid page-specific fonts, colors, or inline styles. Use one page title, numbered headings for sequential setup, and unnumbered headings for reference material. Tables, code blocks, notes, and warnings share the global styles; keep warning colors distinct from informational notes.

Wrap images in `figure.handbook-figure` with a plain-text `figcaption` and a `.figure-links` paragraph. Use **View full-size image** and, when available, **Source photograph** or **Source PDF**. Follow the markup in `docs/unidog-nav/index.md`. Preserve each real image's aspect ratio and existing labels.

Project display names are **VLA Pipeline** and **Self Improvement Learning**. Keep software identifiers (`robocoop`, `unidog_nav`), existing documentation paths, and the configured “Hey UniDog” wake word unchanged unless those underlying systems are renamed.
