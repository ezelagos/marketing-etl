import pandas as pd
import boto3
import os
from io import StringIO

#Configuracion
s3_client = boto3.client('s3')
NOMBRE_BUCKET = 'data-project1-eze-2025'
archivo_salida_key = "marketing_master_dataset.csv"

# 1. LISTAR ARCHIVOS (reemplazo de glob)
#le pedimos a s3 todos los objetos que empiecen con 'marketin_data_'
response = s3_client.list_objects_v2(Bucket=NOMBRE_BUCKET, Prefix='marketing_data_')

lista_dataframes = []

#Verificamos si hay archivos (S3 devuelve la lista en la clave 'Contents)
if 'Contents' in response:
    print(f"Detectados {len(response['Contents'])} archivos en S3. Procesando...")

    for objeto in response['Contents']:
        clave_archivo = objeto['Key'] #Esto es el nombre, ej// "marketing_data_1.csv"

        #AQUI ESTA EL RETO
        #NECESITAMOS LEER EL CONTENIDO DEL ARCHIVO DESDE S3
        #LA FUNCION ES: s3_client.get_object(Bucket=...., Key=...)

        obj_s3 = s3_client.get_object(Bucket=NOMBRE_BUCKET, Key=clave_archivo)

        # 'obj_s3' es un diccionario. El contenido real esta en obj_s3['Body]
        #Pandas puede leer ese 'Body' directamente

        df_temp = pd.read_csv(obj_s3['Body'])
        lista_dataframes.append(df_temp)
    
    #FIN DEL RETO

if lista_dataframes:
    print("Unificando dataframes...")
    df_maestro = pd.concat(lista_dataframes, ignore_index=True)
    #ESTRATEGIA HIBRIDA
    
    # 1. Guardar en LOCAL (para tu inspeccion rapida)
    print(f"Guardando {archivo_salida_key} en disco local...")
    df_maestro.to_csv(archivo_salida_key, index=False)
    # 2. Guardar en S3 (para el datalake/ futuro DWH)
    print(f"Subiendo {archivo_salida_key} a S3...")
    csv_buffer = StringIO()
    df_maestro.to_csv(csv_buffer, index=False) #Escribimos en memoria
    s3_client.put_object(
        Bucket=NOMBRE_BUCKET,
        Key=archivo_salida_key,
        Body=csv_buffer.getvalue()
    )
    print("EXITO - Dataset Maestro sincronizado en Local y Nube")
    
else:
    print("No se encontraron archivos en el bucket con ese prefijo")