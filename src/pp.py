import xarray as xr
import glob
import numpy as np
import matplotlib.pyplot as plt
from aux import *
from datetime import datetime
import multiprocessing as mp

start = datetime.now()
print(f"Emprieza: {start}")

print("Abriendo datos...")
# Abrir los archivos ya descargados
files = glob.glob("./db/WRF*")
ds_list = []
for filename in files:
   ds_tmp = xr.open_dataset(filename, decode_coords = 'all', engine = 'h5netcdf')
   ds_list.append(ds_tmp)

print("Datos abiertos, combinando...")
# Combinamos los archivos en un unico dataset
# We combine all the files in one dataset
ds = xr.combine_by_coords(ds_list, combine_attrs = 'drop_conflicts')

print("Datos combinados, enmascarando...")
# Enmascaro los datos de lluvia < 0.1 mm hr-1
pp = ds[["PP"]]
mask = pp > 0.1
pp_mask = pp.where(mask, np.nan)

# Graficado
print("Graficando...")

def proceso_graficado(tpo):
    f, ax = plt.subplots()

    plot_pp_wrf(ax, pp_mask, tpo, -90, -60, -20, -50)

    plt.savefig("assets/pp/" + str(pp_mask.isel(time=tpo).time.values) + ".png", dpi = 150, bbox_inches = "tight")
    plt.close()

if __name__ == '__main__':
    pool = mp.Pool(3)
    pool.map(proceso_graficado, range(1, 72))

print(f"Fin. Tiempo de proceso: {datetime.now() - start}")