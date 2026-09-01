"""Generate the T6 workbook from the fresh T6 raw output."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("T6_main.py")), run_name="__main__")
