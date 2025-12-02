from airflow import DAG
from airflow.operators.bash import BashOperator  
from datetime import datetime, timedelta

# 1. Configuracion por defecto (Argumentos Comunes)
default_args = {
    'owner': 'ezequiel',                #Tu nombre como dueño del proceso
    'depends_on_past': False,           #Si falla ayer, debe fallar hoy? NO...
    'email_on_failure': False,          #Avisar por mail si explota? por ahora no
    'retries': 1,                       #Si falla, intenta 1 vez mas
    'retry_delay': timedelta(minutes=5) #Espera 5 minutos antes de reintentar
}

# 2. Definicion del DAG (el contenedor)
with DAG(
    'marketing_pipeline_v1', #ID unico del DAG (asi aparecera en la web de AirFlow)
    default_args=default_args,
    description='Pipeline ETL de Marketing: Generar -> Unificar -> Analizar',
    schedule='@daily', #Correr una vez al dia
    start_date=datetime(2024, 1, 1), #Fecha de inicio (poner una pasada para que no arranque ya)
    catchup=False,  #No intentes rellenar los dias pasados no ejecutados
    tags=['marketing','etl'],
) as dag:

    #DEFINICION DE TAREAS
    #Usamos BashOperator porque tus scripts ya funcionan en terminal
    #Airflow simplemente hara de "usuario" ejecutando los comandos por vos

    #IMPORTANTE: cambia ruta por ruta real (pwd en terminal)

    t1_generar = BashOperator(
        task_id='generar_datos_raw',
        bash_command='python3 /home/eze/proyecto_prueba/data_generator.py'
    )

    t2_unificar = BashOperator(
        task_id='unificar_csvs',
        bash_command='python3 /home/eze/proyecto_prueba/data_merger.py'
    )

    t3_analizar = BashOperator(
        task_id='generar_reporte',
        bash_command='python3 /home/eze/proyecto_prueba/data_analysis.py'
    )

    # ORQUESTACION (dependencias)
    #aqui definimos las flechas del diagrama
    #t1 debe terminar OK antes de t2. etc

    t1_generar >> t2_unificar >> t3_analizar