import pickle
import re
from pathlib import Path


__version__ = "28-01-2025-11-30-11.pkl"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_pipeline_{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


