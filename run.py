import subprocess
import logging
from datetime import datetime
import math
#------------<>------------
start = datetime.now()
##--- Logs
logging.basicConfig(filename='logs/proceso_entero.log', level=logging.DEBUG)
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
log.info("---STARTING---")
log.info(f"Time start: {start}")
log.info(f"Seteando argumentos..")
##--- Seteando argumentos de entrada
init_year = 2024
init_month = 6
init_day = 19
init_hour = 0
start_lead_time = 0
end_lead_time = 73
p_salida = "db/"
##----------------------------------
log.info(f"Argumentos seteados..comienza la descarga..")
##--- Ejecucion de la descarga
def run():
    subprocess.run([
        "python",
        "getSmn.py",
        str(init_year),
        str(init_month),
        str(init_day),
        str(init_hour),
        str(start_lead_time),
        str(end_lead_time),
        p_salida
    ])

#--- Ejecucion como main
if __name__ == "__main__":
    run()
    log.info(f"Descarga finalizada.")
    end = datetime.now()
    log.info(f"Time ending: {end}")
    diff = end - start
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    log.info(f"Tiempo de ejecucion: {str(hours).zfill(2)}h:{str(minutes).zfill(2)}min:{str(seconds).zfill(2)}seg")