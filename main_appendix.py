"""Generate Appendix Figures C1-C5."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("Appendix_Fig_main.py")), run_name="__main__")
