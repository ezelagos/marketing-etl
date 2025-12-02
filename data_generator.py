import  pandas      as pd
from    faker       import Faker
import  uuid
import  random
from    datetime    import datetime, timedelta
import  os
from    io          import StringIO

NUM_REGISTROS_TOTAL = 500000
TAMAÑO_LOTE = 10000
FECHA_INICIO = datetime(2024, 1, 1)
FECHA_FIN = datetime(2024,12,31)

#Aseguramos que la carpeta de destino exista
os.makedirs('data', exist_ok=True)

#Inicializamos el generador (Faker)
fake = Faker()

#Nota: aunque definimos 'columnas' arriba en este script dinamico
#las columnas finales dependeran de las claves del dicionario 'dato'

total_registros_generados = 0
numero_lote = 1

print(f" --- INICIANDO PROCESO ETL --- ")
print(f"Meta: {NUM_REGISTROS_TOTAL} registros en lotes de {TAMAÑO_LOTE}")

#Bucle principal(While)
while total_registros_generados < NUM_REGISTROS_TOTAL:
    print(f"Generando lote {numero_lote}...")

    lote_datos = []

    #Bucle secundario (For - Generacion del lote)
    for i in range(TAMAÑO_LOTE):
        
        #calculamos las variables (logica del negocio)
        impresiones_calc = random.randint(1000, 1000000)
        #CTR entre 1% y 5%
        ctr_calc = random.uniform(0.01, 0.05)
        #Clicks derivados de impresiones * CTR (Coherencia de datos)
        clicks_calc = int(impresiones_calc * ctr_calc)
        #CPC entre 0.01, 0.05
        cpc_calc = random.uniform(0.01, 0.50)
        #Costo total derivado
        costo_total_calc = round(clicks_calc * cpc_calc, 2)
        video_view_time_calc = round(random.uniform(0.1, 10.00), 2)

        #Guardamos en diccionario
        dato = {
            "campaign_id": str(uuid.uuid4()),
            "date": fake.date_between(start_date=FECHA_INICIO, end_date=FECHA_FIN),
            "platform": random.choice(['Facebook ADS', 'Google ADS']),
            "target_audience": random.choice([
                'Mujer 18-25', 'Mujer 26-35', 'Mujer 36-45', 'Mujer +46', 
                'Hombre 18-25', 'Hombre 26-35', 'Hombre 36-45', 'Hombre +46'
            ]),
            "impressions": impresiones_calc,
            "ctr": round(ctr_calc, 4), # Redondeamos para que quede bonito en el CSV
            "clicks": clicks_calc,
            "cpc": round(cpc_calc, 2),
            "costo_total": costo_total_calc,
            "video_view_time": video_view_time_calc
        }

        lote_datos.append(dato)
    csv_buffer = StringIO()
    #Convertir lote a DataFrame
    df_lote = pd.DataFrame(lote_datos)

    #Generar nombre unico
    nombre_archivo = f"data/marketing_data_{numero_lote}.csv"

    #Guardar a CSV
    df_lote.to_csv(csv_buffer, index=False)
    print(f" -> Guardado: {nombre_archivo}")

    total_registros_generados += TAMAÑO_LOTE
    numero_lote +=1
print("--- PROCESO FINALIZADO ---")