from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from model import default_run_dir, generate_table

parser = argparse.ArgumentParser(description="Evaluate T5 and generate the paper-format CSV")
parser.add_argument("--run_dir", type=Path, default=default_run_dir())
parser.add_argument("--markets", default="all")
parser.add_argument("--output_dir", type=Path, default=None)
parser.add_argument("--seed", type=int, default=None)
parser.add_argument("--seed_config", type=Path, default=None)
parser.add_argument("--dqn_eval_mode", choices=["dqn"], default="dqn")
parser.add_argument("--no_baselines", action="store_false", dest="include_baselines", default=True)
args = parser.parse_args()
generate_table("T5", run_dir=args.run_dir, markets=args.markets,
               output_dir=args.output_dir, seed=args.seed, seed_config=args.seed_config,
               include_baselines=args.include_baselines, dqn_eval_mode=args.dqn_eval_mode)
