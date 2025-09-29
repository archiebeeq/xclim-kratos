import numpy as np


def basic_qc(ds, drop_missing_threshold=0.1):
    """Run basic QC. Returns cleaned ds and qc_report dict.

    - flag missing values
    - drop rows with all vars missing
    """
    report = {}
    n = ds.sizes.get("time", 0)
    report["n_time"] = int(n)
    report["missing_prec"] = int(ds["prec"].isnull().sum().item())
    report["missing_tmax"] = int(ds["tmax"].isnull().sum().item())
    report["missing_tmin"] = int(ds["tmin"].isnull().sum().item())
    # drop rows where all variables missing
    mask_all_missing = np.isnan(ds["prec"]) & np.isnan(ds["tmax"]) & np.isnan(ds["tmin"]) if n > 0 else np.array([])
    if n > 0 and mask_all_missing.any():
        ds = ds.sel(time=~mask_all_missing)
        report["dropped_all_missing"] = int(mask_all_missing.sum().item())
    else:
        report["dropped_all_missing"] = 0
    return ds, report
