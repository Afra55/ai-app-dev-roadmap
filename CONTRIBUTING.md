# Contributing

## Setup

```bash
git clone https://github.com/Afra55/ai-app-dev-roadmap.git
cd ai-app-dev-roadmap
pip install -e ".[dev]"
cp week1/.env.example week1/.env   # optional: add DEEPSEEK_API_KEY
```

## Checks before PR

```bash
bash scripts/check_portfolio.sh
pytest -q
```

## Code style

- Match existing module naming per week/project
- Put reusable logic in `common/`, not copy-paste across weeks
- Update `CHANGELOG.md` for user-visible changes
- Keep `verify_setup.py` passing without API key where possible

## Documentation

- Fix file paths when renaming modules
- Update root `README.md` if adding top-level directories
