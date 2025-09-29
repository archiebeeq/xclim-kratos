kratos — Python pipeline replacing parts of Climpact

This folder contains a minimal Python pipeline that reads station CSV files (year, month, day, prec, tmax, tmin), performs basic quality control, builds an xarray Dataset and computes a few basic climate indices. The code is intentionally dependency-light; installing xclim is recommended for richer indices.

Quick start (PowerShell)

1. Create and activate a venv, install deps:

```powershell
python -m venv .\kratos\venv
.\kratos\venv\Scripts\Activate.ps1
pip install -r kratos\requirements.txt
```

2. Run the pipeline on your CSV (example):

```powershell
..\kratos\venv\Scripts\python.exe .\scripts\run_pipeline.py "C:\path\to\sydney_observatory_hill_2015-2100_6rowtransofrm.csv" --outdir outputs --plots TXx heavy_precip_days
```

Command-line reference
----------------------

kratos provides a single CLI script at `kratos/scripts/run_pipeline.py`. The basic command shape:

```text
python kratos/scripts/run_pipeline.py <input.csv> [--outdir OUTDIR] [--plots PLOTS [PLOTS ...]] [--plot-strategy STRATEGY] [--plot-config CONFIG]
```

Flags and options
- `input.csv` (positional): Path to a station CSV with columns: `year,month,day,prec,tmax,tmin`. Rows with missing date parts are dropped.
- `--outdir OUTDIR` (default: `kratos_outputs`): Directory where output NetCDF, CSV and PNG files are written.
- `--plots PLOTS [PLOTS ...]`: One or more indices to plot. Examples: `TXx`, `TNn`, `heavy_precip_days`. If omitted, no plots are produced.
- `--plot-strategy STRATEGY` (optional): Global strategy applied to all plots. Example values: `timeseries`, `annual_bar`, `trend`, `threshold_alert`.
- `--plot-config CONFIG` (optional): Per-plot strategy overrides; comma-separated list of `index:strategy` pairs. Example: `heavy_precip_days:annual_bar,TXx:trend`.

Plot strategies (built-ins)
- `timeseries` — line chart of the series (default)
- `annual_bar` — bar chart (good for counts like heavy precip days)
- `trend` — timeseries + rolling mean + linear trend line
- `threshold_alert` — simple highlight of values beyond a specified threshold (can be extended)

Examples
--------

# 1) Produce TXx (annual max tmax) time series and heavy precip bar chart
```powershell
..\kratos\venv\Scripts\python.exe .\scripts\run_pipeline.py "C:\path\to\sydney.csv" --outdir outputs --plots TXx heavy_precip_days --plot-config "heavy_precip_days:annual_bar,TXx:trend"
```

# 2) Global strategy for all plots (useful for quick runs)
```powershell
..\kratos\venv\Scripts\python.exe .\scripts\run_pipeline.py "C:\path\to\sydney.csv" --outdir outputs --plots TXx heavy_precip_days --plot-strategy trend
```

# 3) No plots, just produce NetCDF and CSV indices
```powershell
..\kratos\venv\Scripts\python.exe .\scripts\run_pipeline.py "C:\path\to\sydney.csv" --outdir outputs
```

Outputs produced
----------------
- `outputs/observations.nc` — CF-style NetCDF with variables `prec`, `tmax`, `tmin`, `dtr` and a `time` coordinate.
- `outputs/indices.nc` — NetCDF with annual indices computed by the pipeline (e.g. `TXx`, `TNn`, `heavy_precip_days`).
- `outputs/indices.csv` — CSV table of index values.
- `outputs/<index>.png` — PNG plots for requested indices and strategies.

Extending and customization
---------------------------
- QC rules: extend `kratos/services/qc.py` with additional checks (duplicates, continuity gaps, plausible ranges).
- Indices: replace or extend `kratos/services/compute_indices.py` with xclim-based implementations for climdex-equivalent indices. xclim is already in `requirements.txt`.
- Plot strategies: add new strategies in `kratos/services/plots.py` and expose them via `--plot-strategy`/`--plot-config`.

Troubleshooting
---------------
- Module import errors when running the script directly: run via the venv Python (example above) or ensure the repository root is on `PYTHONPATH`.
- `ValueError: failed to prevent overwriting existing key calendar in attrs on variable 'time'`: fixed by the CLI; if you still see this, ensure you use the provided `run_pipeline.py` in `kratos/scripts` which strips the attribute before writing NetCDF.
- If xclim or other packages fail to install on Windows, ensure you have a C compiler and the appropriate wheels, or temporarily remove `xclim` from `requirements.txt` and rely on the xarray fallbacks.

Development and tests
---------------------
- Unit tests are under `kratos/tests/` and can be run with the venv Python:

```powershell
..\kratos\venv\Scripts\python.exe -m pytest -q kratos\tests\test_pipeline.py
```


Commands to use

### To activate venv
```shell
.\kratos\venv\Scripts\Activate.ps1
```

### To deactivate venv
```shell
deactivate
```

### Run indices script
```shell
.\kratos\venv\Scripts\python.exe .\kratos\scripts\run_pipeline.py "C:\Users\Swensolly Computers\Desktop\climpact-3.3\sydney_observatory_hill_2015-2100_6rowtransofrm.csv" --outdir outputs --plots TNn
```

Contact & next steps
--------------------
If you'd like, I can:
- Implement xclim mappings for the full set of climdex indices you need.
- Add interactive plotting strategies or a small dashboard to pick strategies at runtime.
- Integrate the Python outputs back into the remaining R/Shiny parts of the app.

Feedback: update this README with any domain-specific indices or plotting styles you prefer and I'll wire them in.