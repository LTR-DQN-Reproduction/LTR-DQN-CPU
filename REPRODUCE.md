# CPU reproduction package

This package contains the CPU-only source, raw input data, and the validated
T3/T4/T5/T7, T6, Figures 3-7, and Appendix Figures C1-C5 outputs.

Environment: Python 3.9.13, NumPy 1.21.5, pandas 1.4.4, PyTorch 2.0.0+cpu,
XGBoost 1.7.6. Runtime is locked to one CPU thread by `runtime_config.py`.

From this directory, create the environment from `environment.yml`, activate
it, then run:

```text
python train.py --run_dir . --models all --years 2,3,4 --ranker_tree_method approx --rank_config rank_config.json --t6 --t6_max_seeds 20
python main.py --run_dir . --tables T3,T4,T5,T7 --export_csvs
python T6_main.py --run_dir .
python Fig_main.py --run_dir . --figures 3,4,5,6,7 --ranker_tree_method approx --force
python Appendix_Fig_main.py --run_dir . --figures C1,C2,C3,C4,C5 --force
```

The `results/` directory contains the validated outputs. Figure 4 records its
figure-only fixed parameters in `results/figures/data/Fig4_LambdaMART_hyperparameters.csv`.
