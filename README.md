# Kratos — station-to-indices pipeline

Kratos is a lightweight Python pipeline for processing station CSV files, running basic quality checks, building an xarray Dataset, and computing a set of commonly used daily climate indices (optionally via xclim).

This repository has been refocused to contain the `kratos/` Python project. If you previously used the R-based "Climpact" tools, those sources are no longer part of the primary repository layout.

See `kratos/README.md` for full documentation and examples. The `kratos/` package includes a small CLI (`kratos/scripts/run_pipeline.py`) that reads station CSVs (year, month, day, prcp, tmax, tmin), runs QC, computes indices, and writes NetCDF/CSV/PNG outputs.

Quick start

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r kratos/requirements.txt
```

3. Run the example pipeline (from repo root):

```powershell
python kratos\scripts\run_pipeline.py --input sample_data/station.csv --output outputs
```

See `kratos/README.md` for CLI flags and advanced usage.

Repository notes

- License: see `LICENSE`.
- The `kratos/` directory contains the Python pipeline, tests, and documentation.

If you want the old Climpact R sources removed from the repository entirely (permanently deleted) or moved into an `archive/` folder, tell me which you prefer and I will perform that next step.
