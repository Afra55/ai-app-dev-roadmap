"""Verify Android Gradle wrapper is present and executable."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

ANDROID_APPS = (
    Path("phase1/week3/android-app"),
    Path("phase2/direction-a-smart-notes/android-app"),
    Path("phase2/direction-b-bank-assistant/android-app"),
)


def test_gradle_wrapper_exists():
    root = Path(__file__).resolve().parents[1]
    for rel in ANDROID_APPS:
        app_dir = root / rel
        assert (app_dir / "gradlew").is_file(), f"missing gradlew: {rel}"
        assert (app_dir / "gradle/wrapper/gradle-wrapper.jar").is_file()


def test_gradlew_version_runs():
    root = Path(__file__).resolve().parents[1]
    app_dir = root / ANDROID_APPS[0]
    env = os.environ.copy()
    env.pop("ANDROID_HOME", None)
    result = subprocess.run(
        ["./gradlew", "--version"],
        cwd=app_dir,
        capture_output=True,
        text=True,
        timeout=120,
        env=env,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Gradle 8.9" in result.stdout
