import pandas as pd
from faker import Faker
import uuid
import random
from datetime import datetime, timedelta
import boto3
import os
from io import StringIO

s3_client = boto3.client('s3')
NOMBRE_BUCKET = 'data-project1-eze-2025'

# --- CONFIGURACION ---
NUM_REGISTROS_TOTAL = 500000 
TAMANO_LOTE = 10000
FECHA_INICIO = datetime(2024, 1, 1)
FECHA_FIN = datetime(2024, 12, 31)

# Aseguramos que la carpeta de destino exista
os.makedirs('data', exist_ok=True)

fake = Faker()
total_registros_generados = 0
numero_lote = 1

print(f"--- INICIANDO PROCESO ETL ---")



while total_registros_generados < NUM_REGISTROS_TOTAL:
    lote_datos = []
    for i in range(TAMANO_LOTE):
        # Generamos métricas simuladas
        impresiones_calc = random.randint(1000, 1000000)
        ctr_calc = random.uniform(0.01, 0.05) 
        clicks_calc = int(impresiones_calc * ctr_calc)
        cpc_calc = random.uniform(0.01, 0.50)
        costo_total_calc = round(clicks_calc * cpc_calc, 2)
        video_view_time_calc = round(random.uniform(0.1, 10.00), 2)

        # Creamos el diccionario con los datos
        dato = {
            "campaign_id": str(uuid.uuid4()),
            "date": fake.date_between(start_date=FECHA_INICIO, end_date=FECHA_FIN),
            "platform": random.choice(['Facebook ADS', 'Google ADS']),
            "target_audience": random.choice(['Mujer 18-25', 'Mujer 26-35', 'Mujer 36-45', 'Mujer +46', 'Hombre 18-25', 'Hombre 26-35', 'Hombre 36-45', 'Hombre +46']),
            "impressions": impresiones_calc,
            "ctr": round(ctr_calc, 4),
            "clicks": clicks_calc,
            "cpc": round(cpc_calc, 2),
            "costo_total": costo_total_calc,
            "video_view_time": video_view_time_calc
        }
        
        # ¡Importante! Añadimos el dato a la lista
        lote_datos.append(dato)

    # --- AQUÍ EMPIEZA LA MAGIA CLOUD ---
    
    df_lote = pd.DataFrame(lote_datos)
    
    # 1. Crear el buffer en memoria
    csv_buffer = StringIO()
    
    # 2. Escribir el DataFrame en el buffer
    df_lote.to_csv(csv_buffer, index=False)
    
    # 3. Definir nombre (SIN la carpeta 'data/' para que el Unificador lo encuentre)
    nombre_archivo = f"marketing_data_{numero_lote}.csv"
    
    # 4. Subir a S3
    print(f"☁️ Subiendo {nombre_archivo} a S3...")
    s3_client.put_object(
        Bucket=NOMBRE_BUCKET,
        Key=nombre_archivo,
        Body=csv_buffer.getvalue()
    )
    
    total_registros_generados += TAMANO_LOTE
    numero_lote += 1


print("--- PROCESO FINALIZADO ---")