import pandas as pd
import boto3
from io import StringIO

# --- CONFIGURACIÓN ---
# Usamos el mismo bucket que definimos en los pasos anteriores
NOMBRE_BUCKET = 'data-project1-eze-2025' 
ARCHIVO_CLAVE = "marketing_master_dataset.csv"

def analizar_datos():
    print(f"--- ☁️ DESCARGANDO DATOS DE S3: {ARCHIVO_CLAVE} ---")
    
    s3_client = boto3.client('s3')
    
    try:
        # 1. Traemos el objeto desde S3
        response = s3_client.get_object(Bucket=NOMBRE_BUCKET, Key=ARCHIVO_CLAVE)
        
        # 2. Leemos el contenido (Body) directamente en Pandas
        print("Lectura iniciada...")
        df = pd.read_csv(response['Body'])
        
        # --- ANÁLISIS (Igual que antes) ---
        print("\n📊 --- REPORTE DE MARKETING --- 📊")
        
        # KPI 1: Totales por Plataforma
        plataforma_kpi = df.groupby('platform')[['costo_total', 'clicks', 'impressions']].sum()
        plataforma_kpi['CPC_Real'] = plataforma_kpi['costo_total'] / plataforma_kpi['clicks']
        plataforma_kpi['CTR_Real'] = (plataforma_kpi['clicks'] / plataforma_kpi['impressions']) * 100
        
        print("\n1. Rendimiento por Plataforma:")
        print(plataforma_kpi)
        
        # KPI 2: Audiencia
        print("\n2. Tiempo de visualización por Audiencia:")
        audiencia_view = df.groupby('target_audience')['video_view_time'].mean().sort_values(ascending=False)
        print(audiencia_view)
        
        print("\n✅ Reporte generado exitosamente.")

    except s3_client.exceptions.NoSuchKey:
        print(f"❌ ERROR: El archivo '{ARCHIVO_CLAVE}' no existe en el bucket.")
    except Exception as e:
        print(f"❌ ERROR INESPERADO: {e}")

if __name__ == "__main__":
    analizar_datos()