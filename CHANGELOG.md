# Changelog

## [1.0.0] - 2026-07-01

### Added
- `common/` shared package: LLM client, embeddings, RAG, weather, agent helpers
- `pyproject.toml` for editable install (`pip install -e ".[dev]"`)
- `tests/` pytest suite and GitHub Actions CI
- `docs/ARCHITECTURE.md` architecture guide
- `week5-8/README.md` bridge from weeks 5–8 to `projects/`
- Root `.env.example`, `CONTRIBUTING.md`, portfolio entry in README
- `projects/*/.env.example` for all directions

### Changed
- Root README: unified 12-week navigation with direct links to week1–4 directories
- Added `week1-4/README.md` as Phase 1 navigation hub (symmetric with week5-8, phase3)
- Week READMEs: breadcrumb links back to roadmap and phase overview
- Fixed `week5-8/README.md` broken projects link
- Renamed `test_chat.py` → `demo_chat.py`, `test_rag.py` → `demo_rag.py` (with compatibility shims)
- Week4 `settings.py` documented; added `config.py` re-export alias
- FastAPI apps migrated from `@app.on_event("startup")` to lifespan
- Direction A indexer uses public Chroma delete API via `common.rag`
- Direction A Android adds local greeting fallback when backend offline
- Phase3 interview docs fixed file path references

### Fixed
- Documentation drift (`config.py` vs `settings.py`, shorthand paths)
- `scripts/check_portfolio.sh` and demo script root path resolution
