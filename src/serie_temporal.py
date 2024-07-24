import xarray as xr
import glob
import numpy as np
import matplotlib.pyplot as plt
from aux import *
from datetime import datetime

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

