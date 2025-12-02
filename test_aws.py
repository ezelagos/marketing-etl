import boto3
from botocore.exceptions import ClientError

def probar_conexion_segura():
    # Tu bucket específico
    bucket_nombre = "data-project1-eze-2025"
    
    print(f"📡 Verificando acceso al bucket exclusivo: {bucket_nombre}...")
    
    try:
        s3 = boto3.client('s3')
        
        # Intentamos listar los objetos DENTRO de tu bucket (Esto sí está permitido: s3:ListBucket)
        respuesta = s3.list_objects_v2(Bucket=bucket_nombre, MaxKeys=5)
        
        print("✅ ¡Conexión Exitosa!")
        print(f"Logramos entrar al bucket '{bucket_nombre}'.")
        print("Archivos encontrados:", respuesta.get('KeyCount', 0))
            
    except Exception as e:
        print("❌ Error de conexión:")
        print(e)

if __name__ == "__main__":
    probar_conexion_segura()