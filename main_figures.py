"""Generate main-text Figures 3-7."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("Fig_main.py")), run_name="__main__")
