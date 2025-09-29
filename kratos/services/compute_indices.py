import xarray as xr


def compute_basic_indices(ds):
    """Compute common indices (annual) and return dataset of indices.

    Uses plain xarray so it works even if xclim isn't installed.
    """
    # Resample to annual frequency (year-ending) and compute summaries
    txx = ds["tmax"].resample(time="1Y").max(dim="time", skipna=True)
    tnn = ds["tmin"].resample(time="1Y").min(dim="time", skipna=True)
    heavy = (ds["prec"] >= 10.0).resample(time="1Y").sum(dim="time", skipna=True)
    out_ds = xr.Dataset({
        "TXx": txx,
        "TNn": tnn,
        "heavy_precip_days": heavy
    })
    return out_ds
