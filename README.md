# dylanjoo.github.io

Personal academic website of Jia-Huei (Dylan) Ju, built with [al-folio](https://github.com/alshedivat/al-folio) v1.

## Where things live

| What | File |
| --- | --- |
| Bio, profile photo, address | `_pages/about.md`, `assets/img/prof_pic.jpg` |
| Publications | `_bibliography/papers.bib` (`selected = {true}` → shown on the home page) |
| News items | `_news/*.md` |
| Projects | `_projects/*.md` |
| Social links | `_data/socials.yml` |
| CV / legacy PDFs | `files/` |
| Site settings | `_config.yml` |

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and pushes it to the `gh-pages` branch.
GitHub Pages must be set to **Deploy from a branch → `gh-pages`**.

## Local preview

Requires Ruby >= 3.1 (or Docker):

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

See the upstream [al-folio docs](https://github.com/alshedivat/al-folio/tree/main/docs) for customization.
