import sys
from pathlib import Path

# rend le package src/ importable par pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))