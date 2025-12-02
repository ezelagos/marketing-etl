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

¡Eso está genial! Tienes una visión muy clara del flujo de datos. Has tocado los puntos críticos: Particionamiento, Ingesta Cloud, Transformación y Entrega de Valor (KPIs).

Para el README.md, vamos a darle un toque visual usando Mermaid (una herramienta que GitHub renderiza automáticamente como un diagrama de flujo) y luego explicaremos tus puntos con un lenguaje técnico pulido.

Aquí tienes la sección de Arquitectura lista para copiar. Fíjate cómo transformamos tus puntos en un flujo profesional:

Markdown

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



## 🚀 Instalación y Uso

### Prerrequisitos
* Python 3.10+
* Cuenta de AWS activa (con Access Keys creadas)
* Docker (opcional, si se desea containerizar a futuro)

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/nombre-del-repo.git](https://github.com/TU_USUARIO/nombre-del-repo.git)
cd nombre-del-repo


CONFIGURACION ENTORNO VIRTUAL
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configurar Credenciales AWS
aws configure
# Ingresa tu Access Key ID, Secret Key y Región (ej: us-east-1)

EJECUTAR PIPELINE
iniciar AIRFLOW y EJECUTAR DAG
airflow standalone
# O ejecutar los scripts manualmente para testing:
python3 marketing_data_gen.py
python3 data_merger.py

CREADO POR EZEQUIEL LAGOS