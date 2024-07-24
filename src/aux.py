
def plot_pp_wrf(ax, xarray_df, tpo, lw, le, ln, ls):
    import geopandas as gpd

    sud = gpd.read_file("../DOC/rpfs/db/shps/Sudamérica.shp")

    xarray_df.PP.isel(time=tpo).plot.pcolormesh(cmap = "jet", x = "lon", y = "lat", vmax = 10, ax = ax)

    sud.plot(ax = ax, facecolor = "None")

    ax.set_xlim(lw, le)
    ax.set_ylim(ls, ln)

    ax.set_title("WRF-SMN \n" + str(xarray_df.isel(time=tpo).time.values))

    return(ax)