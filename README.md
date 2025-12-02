# 🚀 Proyecto de Integración de Datos: Marketing ETL Pipeline

## 📋 Descripción del Proyecto
Este proyecto simula un entorno empresarial real implementando un **Pipeline ETL (Extract, Transform, Load)** de extremo a extremo. 

El sistema genera una base de datos ficticia de marketing (simulando campañas de ADS), procesa y normaliza los datos, y los carga bajo una estrategia híbrida: almacenamiento en **AWS S3** (Data Lake) y persistencia local. Todo el flujo es orquestado automáticamente mediante **Apache Airflow**, garantizando la generación diaria de reportes de ventas y métricas clave (KPIs).

### 🎯 Objetivos Principales
* **Ingesta de Datos:** Generación automatizada de datasets masivos.
* **Transformación:** Limpieza y unificación de datos con Pandas.
* **Cloud Computing:** Integración con AWS S3 para almacenamiento escalable.
* **Orquestación:** Automatización de tareas y dependencias con Airflow.
* **Análisis:** Cálculo de métricas de negocio (CPC, CTR, ROI).

## 🛠 Tecnologías Utilizadas

### Infraestructura y Orquestación
* ![Ubuntu](https://img.shields.io/badge/Ubuntu_WSL-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) **WSL: Ubuntu 22.04**: Entorno de desarrollo local.
* ![AWS](https://img.shields.io/badge/AWS_S3-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) **AWS S3**: Almacenamiento en la nube (Data Lake).
* ![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white) **Apache Airflow**: Orquestación de tareas y manejo de dependencias.

### Lenguaje y Librerías (Python)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

* **Manipulación de Datos:** `pandas` 🐼 (Transformación y limpieza).
* **Conexión Cloud:** `boto3` ☁️ (SDK de AWS para Python).
* **Generación de Datos:** `Faker`, `random`, `uuid` (Simulación de datos de marketing realistas).
* **Manejo de Sistema y Tiempo:** `os`, `datetime`.
* **Optimización:** `io.StringIO` (Manejo de buffers en memoria para evitar I/O en disco).

## 🏗️ Arquitectura del Pipeline

El flujo de datos sigue una arquitectura ETL automatizada que conecta un entorno local (WSL) con la nube (AWS).

```mermaid
graph TD;
    A[🐍 Generador de Datos] -->|Lotes CSV| B(☁️ AWS S3: Data Lake);
    B -->|Lectura Raw Data| C[🐼 Transformación & Unificación];
    C -->|Master Dataset| B;
    C -->|Persistencia Local| D[📁 Local Storage];
    B -->|Download| E[📊 Motor de Análisis];
    E -->|KPIs & Métricas| F[📑 Reporte Final];
    
    subgraph Orquestación [Apache Airflow DAG]
    A --> C --> E
    end
Flujo de Datos Detallado
Generación y Particionamiento:

Se crean datos sintéticos de campañas de marketing utilizando Faker.

Los datos se generan en particiones/lotes para simular una ingesta masiva y optimizar el uso de memoria RAM (streaming buffers).

Ingesta al Data Lake (S3):

Carga automática de los archivos crudos (raw data) a un bucket de AWS S3, asegurando la disponibilidad y durabilidad de la información histórica.

Integración (ETL):

El proceso detecta los nuevos archivos en la nube, los descarga y unifica en un Master Dataset.

Se aplica una estrategia de persistencia híbrida, guardando el dataset procesado tanto en S3 (para consumo futuro) como en local (para validación inmediata).

Automatización con Airflow:

Un DAG (marketing_pipeline_v1) coordina la ejecución secuencial de los scripts, manejando dependencias y reintentos ante fallos.

Análisis y Reporte:

Cálculo automatizado de KPIs de negocio: CPC Real, CTR, y tiempo de visualización por audiencia.

Generación de un informe final en consola para la toma de decisiones.

🚀 Instalación y Ejecución
Sigue estos pasos para desplegar el pipeline en tu entorno local.

Prerrequisitos 📋
Python 3.10 o superior.

Una cuenta de AWS activa con un bucket S3 creado.

Credenciales de AWS (Access Key ID y Secret Access Key) con permisos para S3 (AmazonS3FullAccess o similar).

Paso 1: Clonar el repositorio 📥
Bash

git clone [https://github.com/ezelagos/marketing-etl.git](https://github.com/ezelagos/marketing-etl.git)
cd marketing-etl
Paso 2: Configurar el entorno virtual 🐍
Es recomendable usar un entorno virtual para aislar las dependencias.

Bash

# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno
source venv/bin/activate
Paso 3: Instalar dependencias 📦
Bash

pip install -r requirements.txt
Paso 4: Configurar credenciales de AWS ☁️
El proyecto usa boto3 para conectarse a AWS. Configura tus credenciales localmente:

Bash

aws configure
# Ingresa tu AWS Access Key ID, AWS Secret Access Key, y tu región por defecto (ej. us-east-1).
Paso 5: Inicializar Airflow 🌬️
Configura la base de datos y crea un usuario administrador para Airflow.

Bash

# Inicializar la base de datos
airflow db init

# Crear un usuario admin (cambia los valores según prefieras)
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org \
    --password admin
Paso 6: Ejecutar el Pipeline ▶️
Puedes iniciar el servidor web y el scheduler de Airflow en una sola terminal para pruebas locales.

Bash

airflow standalone
Abre tu navegador en http://localhost:8080.

Inicia sesión con el usuario admin que creaste.

Busca el DAG marketing_pipeline_v1, actívalo (ON) y ejecútalo (Trigger DAG).



CREADO POR EZEQUIEL LAGOS
