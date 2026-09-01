from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model import default_run_dir, generate_table

parser = argparse.ArgumentParser(description="Evaluate T7 ESG strategies and generate the CSV")
parser.add_argument("--run_dir", type=Path, default=default_run_dir())
parser.add_argument("--markets", default="all")
parser.add_argument("--output_dir", type=Path, default=None)
parser.add_argument("--seed", type=int, default=None)
parser.add_argument("--seed_config", type=Path, default=None)
args = parser.parse_args()
generate_table("T7", run_dir=args.run_dir, markets=args.markets,
               output_dir=args.output_dir, seed=args.seed, seed_config=args.seed_config)
