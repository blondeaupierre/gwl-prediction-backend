from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import wells, history, forecasts_xgb, forecasts_tabicl_zero_shot, test_results_xgb, \
    test_results_tabicl_zero_shot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://meteonappes.fr",
                   "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Groundwater API"
    }


@app.get("/wells")
def get_wells():
    return wells.to_dict(
        orient="records"
    )


@app.get("/wells/{well_id:path}/history")
def get_history(well_id: str):
    result = history[
        history["well_id"] == well_id
        ]

    return result.to_dict(
        orient="records"
    )


@app.get("/wells/{well_id:path}/test/xgb")
def get_test_results_xgb(well_id: str):
    result = test_results_xgb[
        test_results_xgb["well_id"] == well_id
        ]

    return result.to_dict(
        orient="records"
    )


@app.get("/wells/{well_id:path}/test/tabicl/zero-shot")
def get_test_results_tabicl_zero_shot(well_id: str):
    result = test_results_tabicl_zero_shot[
        test_results_tabicl_zero_shot["well_id"] == well_id
        ]

    return result.to_dict(
        orient="records"
    )


@app.get("/wells/{well_id:path}/forecast/xgb")
def get_forecast_xgb(well_id: str):
    result = forecasts_xgb[
        forecasts_xgb["well_id"] == well_id
        ]

    return result.to_dict(
        orient="records"
    )


@app.get("/wells/{well_id:path}/forecast/tabicl/zero-shot")
def get_forecast_tabicl_zero_shot(well_id: str):
    result = forecasts_tabicl_zero_shot[
        forecasts_tabicl_zero_shot["well_id"] == well_id
        ]

    return result.to_dict(
        orient="records"
    )
