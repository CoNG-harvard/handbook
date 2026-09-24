# CoNG Handbook

Source for the CoNG lab's project manuals, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published with GitHub Pages at <https://cong-harvard.github.io/handbook/>.

## Preview locally

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000, reloads on save
```

## Layout

| Path | What it is |
|---|---|
| `docs/index.md` | Landing page, one card per project |
| `docs/<project>/` | One folder per project; images go in `docs/<project>/assets/` |
| `mkdocs.yml` | Theme and navigation; each top-level `nav` entry becomes a tab |
| `.github/workflows/pages.yml` | Builds the site and publishes it to GitHub Pages |

## Adding a project

1. Create `docs/<project>/index.md` plus any further pages, using relative links.
2. Add a top-level entry for it under `nav:` in `mkdocs.yml`.
3. Add a card for it to `docs/index.md`.
4. Replace private details (LAN IPs, device serials, `/home/<user>/` paths) with placeholders such as `<ROBOT_IP>`.
5. Check that `mkdocs build --strict` passes. It fails on broken links.

## Deployment

Every push to `main` runs `.github/workflows/pages.yml`, which runs `mkdocs build --strict` and publishes `site/` to GitHub Pages. A failed build (for example a broken link) leaves the previous version live. Build logs are in the repo's **Actions** tab.

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
