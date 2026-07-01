# Changelog

## [1.0.0] - 2026-07-01

### Added
- `common/` shared package: LLM client, embeddings, RAG, weather, agent helpers
- `pyproject.toml` for editable install (`pip install -e ".[dev]"`)
- `tests/` pytest suite and GitHub Actions CI
- `docs/ARCHITECTURE.md` architecture guide
- `phase2/README.md` bridge from weeks 5–8 to `phase2/`
- Root `.env.example`, `CONTRIBUTING.md`, portfolio entry in README
- `phase2/*/.env.example` for all directions

### Changed
- Root README: expanded 12-week guide with per-week tasks, deliverables, and verification steps
- **BREAKING**: Repository layout is now `phase1/` + `phase2/` + `phase3/` (was `week1-4/` + `projects/` at root)
- Root README: unified 12-week navigation with direct links to phase directories
- Added `phase1/README.md` as Phase 1 navigation hub (symmetric with phase2, phase3)
- Week READMEs: breadcrumb links back to roadmap and phase overview
- Fixed `phase2/README.md` broken projects link
- Renamed `test_chat.py` → `demo_chat.py`, `test_rag.py` → `demo_rag.py` (with compatibility shims)
- Week4 `settings.py` documented; added `config.py` re-export alias
- FastAPI apps migrated from `@app.on_event("startup")` to lifespan
- Direction A indexer uses public Chroma delete API via `common.rag`
- Direction A Android adds local greeting fallback when backend offline
- Phase3 interview docs fixed file path references

### Fixed
- Documentation drift (`config.py` vs `settings.py`, shorthand paths)
- `scripts/check_portfolio.sh` and demo script root path resolution
