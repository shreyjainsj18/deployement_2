# tests/conftest.py
import sys
from pathlib import Path

# add project root to import search path once for all tests
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
