import pandas as pd
import xarray as xr
import numpy as np
import cftime


def df_to_xr(ds_df, calendar="gregorian", time_name="time"):
    """Convert DataFrame with year/month/day and columns prec,tmax,tmin to xarray.Dataset.

    Uses pandas datetime for gregorian or cftime for non-standard calendars.
    """
    # attempt pandas datetime creation
    try:
        time_index = pd.to_datetime(dict(year=ds_df["year"].astype(int),
                                         month=ds_df["month"].astype(int),
                                         day=ds_df["day"].astype(int)))
        use_cftime = False
    except Exception:
        use_cftime = True
        times = []
        for y, m, d in zip(ds_df["year"], ds_df["month"], ds_df["day"]):
            try:
                times.append(cftime.DatetimeGregorian(int(y), int(m), int(d)))
            except Exception:
                times.append(None)
        mask = [t is not None for t in times]
        ds_df = ds_df.loc[mask].reset_index(drop=True)
        time_index = np.array([t for t in times if t is not None], dtype=object)

    # build dataset
    data_vars = {
        "prec": ("time", ds_df["prec"].astype(float).to_numpy()),
        "tmax": ("time", ds_df["tmax"].astype(float).to_numpy()),
        "tmin": ("time", ds_df["tmin"].astype(float).to_numpy()),
    }
    coords = {time_name: ("time", time_index)}
    ds = xr.Dataset(data_vars=data_vars, coords=coords)

    # set units/attrs
    ds["prec"].attrs.update({"units": "mm", "standard_name": "precipitation_amount"})
    ds["tmax"].attrs.update({"units": "degC", "long_name": "tmax"})
    ds["tmin"].attrs.update({"units": "degC", "long_name": "tmin"})

    # time calendar attr (CF)
    try:
        ds[time_name].attrs["calendar"] = calendar
    except Exception:
        pass

    # derived variable: diurnal temperature range
    ds["dtr"] = ds["tmax"] - ds["tmin"]
    ds["dtr"].attrs["units"] = ds["tmax"].attrs["units"]
    return ds
