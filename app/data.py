import os
import pandas as pd

DATA_DIR = os.path.join(
    os.path.dirname(__file__),
    "../data"
)

wells = pd.read_parquet(
    os.path.join(DATA_DIR, "wells.parquet")
)

history = pd.read_parquet(
    os.path.join(DATA_DIR, "history.parquet")
)

test_results_xgb = pd.read_parquet(
    os.path.join(DATA_DIR, "test_results_xgb.parquet")
)

test_results_tabicl_zero_shot = pd.read_parquet(
    os.path.join(DATA_DIR, "test_results_tabicl_zero_shot.parquet")
)


forecasts_xgb = pd.read_parquet(
    os.path.join(DATA_DIR, "forecasts_xgb.parquet")
)

forecasts_tabicl_zero_shot = pd.read_parquet(
    os.path.join(DATA_DIR, "forecasts_tabicl_zero_shot.parquet")
)

wells["well_id"] = wells["well_id"].astype(str)
history["well_id"] = history["well_id"].astype(str)
test_results_xgb["well_id"] = test_results_xgb["well_id"].astype(str)
test_results_tabicl_zero_shot["well_id"] = test_results_tabicl_zero_shot["well_id"].astype(str)
forecasts_xgb["well_id"] = forecasts_xgb["well_id"].astype(str)
forecasts_tabicl_zero_shot["well_id"] = forecasts_tabicl_zero_shot["well_id"].astype(str)