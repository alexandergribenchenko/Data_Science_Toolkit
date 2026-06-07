# Virtual enviroments

## A. Ambientes vituales con venv (alternativa previa a uv)

- `python -m venv venv`: crear un entorno virtual.
- `.\venv\Scripts\Activate.ps1`: activar el entorno virtual.
- `pip install pandas numpy`: installar las dependencias necesarias con pip.
- `pip list`: verificar que las dependencias estan instaladas.

## B. Instalar `uv`
- `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`: intalar entorno virtual usando powershell.
- `uv --version`: verificar que esta instalado viendo su versión.
- `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`: 

## C. Comabdos `uv`
- `uv venv`: crea un entorno virtual de Python, igual que `python -m venv venv`.
- `.venv\Scripts\activate`: activa el entorno virtual.

- `uv init`: inicializar proyecto.
- `uv add pandas numpy`: incluye las dependencias que necesitemos.
- `uv remove numpy`: elimina las dependencias que necesitemos.
- `uv tree`: me muestras las relaciones entre las dependencias.
- `uv run main.py`: genera el ambiente con todas las dependencias y ejecuta el archivo.
- `uv sync`: solo genera el entorno virtual pero no ejecuta el archivo.
- `uv init [nombre_proyecto]`: inicializar proyecto

- ```C:\Users\User\Desktop\POC_Dagster\project-dagster-university\dagster_university\dagster_essentials>```
- ```pip install uv```

# 01. Dagster - Comandos generales
- `dagster`: Muestra todas las opciones de dagster
- `dagster --version` ó `dagster -v` : Versión de dagster instalada.
- `dagster --help`: ayuda general de dagster.
- `dagster [comando_de_interes] --help`: muestra la ayuda para un comando en específico.
   * Ejemplo: `dagster asset --help`
 
# 02. Dagster - Comandos
- `dagster project scaffold --name car_data`: crea un proyecto nuevo con la estructura base (scaffolding) que Dagster recomienda.
- `dagster dev`: sirve para levantar el entorno de desarrollo de Dagster en tu máquina local.

# 03. Ejemplo Youtube
- instalar uv
- `uv venv`: crear un ambiente virtual con uv.
- `.venv\Scripts\activate`: activar ese ambiente virtual.
- `uv pip install dagster dagster-webserver polars duckdb`: instalar las dependencias necesarias. 
- `dagster project scaffold --name car_data`: crea un proyecto nuevo con la estructura base (scaffolding) que Dagster recomienda.
- `cd .\car_data\`: entramos al folder del proyecto.
- Crear la carpeta de `data` al interior.
- Cambimos nuestros assets en el archivo `assets.py`
- `dagster dev`: dagster dev levanta el servidor de desarrollo de Dagster



# 04. Archivos de ejemplo de tutorial de youtube

## 04.01. `definitions.py`
```python
from dagster import Definitions, load_assets_from_modules
from car_data import assets  # noqa: TID252
from .jobs import car_price_job
from .schedule import car_price_schedule

all_assets = load_assets_from_modules([assets])
all_jobs = [car_price_job]
all_schedules = [car_price_schedule]

defs = Definitions(
    assets=all_assets,
    jobs=all_jobs,
    schedules=all_schedules,
)
```

## 04.02. `assets.py`
```python
import dagster as dg
import polars as pl
import duckdb 
# from sklearn.linear_model import LinearRegression
# @dg.asset
# def hello(context: dg.AssetExecutionContext):
#     context.log.info("Hello!")

# @dg.asset(deps=[hello])
# def world(context: dg.AssetExecutionContext):
#     context.log.info("World!")

# defs = dg.Definitions(assets=[hello, world])

csv_url = 'https://raw.githubusercontent.com/Azure/carprice/refs/heads/master/dataset/carprice.csv'
csv_path = 'data/carprice.csv'

duckdb_path = 'data/car_data.duckdb'
table_name = 'avg_price_per_brand'

@dg.asset
def car_data_file(context: dg.AssetExecutionContext):
    """Download csv"""
    context.log.info('Downloading csv file')
    df = pl.read_csv(csv_url)
    df = df.with_columns([
        pl.col('normalized-losses').cast(pl.Float64, strict=False),
        pl.col('price').cast(pl.Float64, strict=False)
        ])
    df.write_csv(csv_path)

@dg.asset(deps=[car_data_file])
def avg_price_table(context: dg.AssetExecutionContext):
    """Computes average  car price per brand and stores it in duckdb"""
    context.log.info('Creating aggregated duckdb table')
    df = pl.read_csv(csv_path)
    df = df.drop_nulls(['price'])

    # Compute average price per brand
    avg_price_df = df.group_by(('make')).agg(
        pl.col('price').mean().alias('avg_price')
        )
    
    # store in duckdb
    # Convert data to list of tuples (DuckDB expects this format)
    data = data = [(row["make"], row["avg_price"]) for row in avg_price_df.to_dicts()]

    with duckdb.connect(duckdb_path) as con:
        con.execute(f"DROP TABLE IF EXISTS {table_name}")
        con.execute(f"CREATE TABLE {table_name} (make TEXT, avg_price DOUBLE)")

        # Insert data
        con.executemany(f"INSERT INTO {table_name} (make, avg_price) VALUES (?, ?)", data)
```

## 04.03. `jobs.py`
```python
import dagster as dg

car_price_job = dg.define_asset_job(
    name="car_price_job",
    selection=dg.AssetSelection.all()
)
```

## 04.04. `schedule.py`
```python
import dagster as dg
from .jobs import car_price_job

car_price_schedule = dg.ScheduleDefinition(
    job=car_price_job,
    cron_schedule="* * * * *", # every minute
)
```
