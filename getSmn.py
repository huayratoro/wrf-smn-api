import s3fs
import datetime
from multiprocessing import Pool, set_start_method
import argparse
##----------- Param de entrada -----------
parser = argparse.ArgumentParser(description="Una funcion que descarga las saldas horarias del WRF-SMN desde un repo AWS publico")
parser.add_argument("iy", type = str, help = "Year inicial")
parser.add_argument("im", type = str, help = "Mes inicial")
parser.add_argument("id", type = str, help = "Dia inicial")
parser.add_argument("ih", type = str, help = "Hora inicial")
parser.add_argument("slt", type = str, help = "Start Lead Time", default=0, choices=["0", "6", "18"])
parser.add_argument("eld", type = str, help = "End Lead Time")
parser.add_argument("ps", type = str, help= "Ruta de guardado de archivos")
args = parser.parse_args()
##----------- Param de entrada -----------

## descarga directamente los datos del AWS
def download_wrf_s3fs(fs, s3_file, p_salida):
   if fs.exists(s3_file):
       f = fs.get(s3_file, p_salida)
   else:
       print('The file {} does not exist'.format(s3_file))

## inicia el proceso de descarga de los datos
def getWrf(init_year, init_month, init_day, init_hour, start_lead_time, end_lead_time, p_salida):
    # seteo las credenciales
    fs = s3fs.S3FileSystem(anon=True)
    # rutas donde estan las salidas de los modelos
    INIT_DATE = datetime.datetime(init_year, init_month, init_day, init_hour)
    files = [f'smn-ar-wrf/DATA/WRF/DET/{INIT_DATE:%Y/%m/%d/%H}/WRFDETAR_01H_{INIT_DATE:%Y%m%d_%H}_{fhr:03d}.nc' for fhr in range(start_lead_time, end_lead_time)]
    # descargo
    if __name__ == "__main__":
        set_start_method("spawn")
        with Pool(5) as pool:
            args = [(fs, file, p_salida) for file in files]
            pool.starmap(download_wrf_s3fs, args)

## ejecuta el proceso de descarga de los datos
def main():
    getWrf(
        int(args.iy),
        int(args.im),
        int(args.id),
        int(args.ih),
        int(args.slt),
        int(args.eld), 
        args.ps
    )

if __name__ == "__main__":
    main()