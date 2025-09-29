import matplotlib.pyplot as plt


def plot_index(ds_index, index_name, outpath=None):
    series = ds_index[index_name]
    fig, ax = plt.subplots(figsize=(8,4))
    try:
        series.plot(ax=ax, marker='o')
    except Exception:
        ax.plot(series.values)
    ax.set_title(index_name)
    ax.set_ylabel(series.attrs.get("units", ""))
    if outpath:
        fig.savefig(outpath, bbox_inches="tight")
    plt.close(fig)
    return outpath
