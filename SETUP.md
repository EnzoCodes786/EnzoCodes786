# Setup Notes

This repo is meant to live at **github.com/EnzoCodes786/EnzoCodes786** (a GitHub profile
README repo — same name as your username, so GitHub renders README.md on your profile page).

## 1. Push it as your profile repo
```bash
cd github-profile
git init
git remote add origin https://github.com/EnzoCodes786/EnzoCodes786.git
git add .
git commit -m "chore: initial profile setup"
git branch -M main
git push -u origin main
```
If `EnzoCodes786/EnzoCodes786` doesn't exist yet, create it first on GitHub (public repo,
same name as your username) — GitHub will show a banner confirming it'll appear on your profile.

## 2. Fill in placeholder links
In `README.md`, swap the `(#)` links for:
- Portfolio URL
- LinkedIn URL
- Email (`mailto:you@example.com`)

Repo links under **Featured Projects** currently point to
`github.com/EnzoCodes786/<repo-name>` — update any that don't match your actual repo names.

## 3. Enable the workflows
All three workflows in `.github/workflows/` run automatically once pushed. No action needed
for `snake.yml` or `update-readme.yml` — they use the default `GITHUB_TOKEN`.

`update-stats.yml` (the `lowlighter/metrics` action) needs a **Personal Access Token** with
`repo` and `read:user` scopes, since the default token can't read account-wide stats:
1. Generate one at Settings → Developer settings → Personal access tokens.
2. In this repo: Settings → Secrets and variables → Actions → New repository secret.
3. Name it `METRICS_TOKEN` and paste the token.

## 4. First run
Trigger each workflow once manually from the **Actions** tab (`Run workflow`) so the initial
`assets/snake-dark.svg` and `assets/metrics.svg` get generated instead of waiting for the
first scheduled run.

## 5. Stats services used
| Section | Service |
|---|---|
| Typing header | readme-typing-svg.demolab.com |
| Stats / top languages | github-readme-stats.vercel.app |
| Streak | github-readme-streak-stats.herokuapp.com |
| Contribution graph | github-readme-activity-graph.vercel.app |
| Contribution snake | Platane/snk |
| LeetCode card | leetcard.jacoblin.cool |
| Visitor counter | komarev.com/ghpvc |

These are free public instances shared across many profiles — if one is slow or rate-limited,
each project has self-host instructions in its own repo.
