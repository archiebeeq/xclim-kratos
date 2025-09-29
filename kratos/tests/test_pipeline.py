from kratos.services.read_transform import read_csv_to_df
from kratos.services.dataset_builder import df_to_xr
from kratos.services.compute_indices import compute_basic_indices
import os

def test_pipeline_minimal(tmp_path):
    # create a tiny CSV
    csv = tmp_path / "test.csv"
    csv.write_text("year,month,day,prec,tmax,tmin\n2000,1,1,0.0,20.0,10.0\n2000,1,2,5.0,21.0,11.0\n")
    df = read_csv_to_df(str(csv))
    ds = df_to_xr(df)
    indices = compute_basic_indices(ds)
    assert "TXx" in indices
    assert indices.sizes["time"] == 1
