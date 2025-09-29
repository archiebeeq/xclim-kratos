"""Simple CLI to run the kratos pipeline."""
import sys
import pathlib
import argparse
import os

# Make imports robust when running this script from inside the kratos/ folder
# by adding the repository root to sys.path. This allows "python scripts/run_pipeline.py"
# to work regardless of current working directory.
repo_root = pathlib.Path(__file__).resolve().parents[2]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from kratos.services.read_transform import read_csv_to_df
from kratos.services.dataset_builder import df_to_xr
from kratos.services.qc import basic_qc
from kratos.services.compute_indices import compute_basic_indices
from kratos.services.plots import plot_index


def main(infile, outdir, plots):
    os.makedirs(outdir, exist_ok=True)
    print(f"Reading {infile}")
    df = read_csv_to_df(infile)
    ds = df_to_xr(df)
    ds, qc_report = basic_qc(ds)
    obs_path = os.path.join(outdir, "observations.nc")
    # xarray/netCDF encoding will raise if 'calendar' exists in attrs on the time
    # variable; remove it before serializing and keep a copy to avoid mutating ds.
    try:
        ds_to_save = ds.copy()
        if "time" in ds_to_save.coords and "calendar" in ds_to_save["time"].attrs:
            ds_to_save["time"].attrs.pop("calendar", None)
        ds_to_save.to_netcdf(obs_path)
    except Exception:
        # fallback: remove attribute in-place and retry
        if "time" in ds.coords:
            ds["time"].attrs.pop("calendar", None)
        ds.to_netcdf(obs_path)
    print("Saved observations to", obs_path)
    indices = compute_basic_indices(ds)
    idx_path = os.path.join(outdir, "indices.nc")
    try:
        indices_to_save = indices.copy()
        if "time" in indices_to_save.coords and "calendar" in indices_to_save["time"].attrs:
            indices_to_save["time"].attrs.pop("calendar", None)
        indices_to_save.to_netcdf(idx_path)
    except Exception:
        if "time" in indices.coords:
            indices["time"].attrs.pop("calendar", None)
        indices.to_netcdf(idx_path)
    indices.to_dataframe().to_csv(os.path.join(outdir, "indices.csv"))
    print("Saved indices to", idx_path)
    for p in plots:
        outpath = os.path.join(outdir, f"{p}.png")
        plot_index(indices, p, outpath)
        print("Wrote plot:", outpath)
    print("QC report:", qc_report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("--outdir", default="kratos_outputs")
    parser.add_argument("--plots", nargs="*", default=["TXx"])
    args = parser.parse_args()
    main(args.infile, args.outdir, args.plots)
