"""Tests for common.paths helpers."""

from __future__ import annotations

from common.paths import PHASE1_DIR, PHASE2_DIR, PHASE3_DIR, REPO_ROOT, project_dir, week_dir


def test_repo_root_contains_phases():
    assert (REPO_ROOT / "phase1").is_dir()
    assert (REPO_ROOT / "phase2").is_dir()
    assert (REPO_ROOT / "phase3").is_dir()


def test_week_dir_points_to_phase1():
    assert week_dir("week1") == PHASE1_DIR / "week1"
    assert week_dir("week4") == PHASE1_DIR / "week4"


def test_project_dir_points_to_phase2():
    assert project_dir("direction-a-smart-notes") == PHASE2_DIR / "direction-a-smart-notes"
