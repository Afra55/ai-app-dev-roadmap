"""Week 3 configuration."""

from pathlib import Path

WEEK3_DIR = Path(__file__).resolve().parent
MODELS_DIR = WEEK3_DIR / "models"

# Small Qwen2.5 model suitable for CPU demo and on-device learning.
DEFAULT_MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
MAX_NEW_TOKENS = 256
TEMPERATURE = 0.7
