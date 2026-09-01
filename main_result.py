"""Generate result tables T3, T4, T5 and T7."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("main.py")), run_name="__main__")
