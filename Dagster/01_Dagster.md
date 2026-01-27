# Dagster Test

# 02. Archivos de ejemplo de tutorial de youtube

## 02.01. `definitions.py`
```python
# dags/definitions.py
from dagster import Definitions, EnvVar, load_assets_from_modules
from dags import assets
from dagster_azure.adls2 import ADLS2Resource, ADLS2SASToken

all_assets = load_assets_from_modules([assets])

resources = {
    "adls2": ADLS2Resource(
        storage_account=EnvVar("ADLS2_STORAGE_ACCOUNT"),
        credential=ADLS2SASToken(token=EnvVar("ADLS2_SAS_TOKEN")),
    )
}

defs = Definitions(
    assets=all_assets,
    resources=resources
)
```

## 02.02. `assets.py`

```python
# dags/assets.py
import os
import json
from datetime import datetime, timezone
import dagster as dg
from dagster_azure.adls2 import ADLS2Resource
from integrations.config import OperaSettings
from integrations.factory import build_opera_client
from zoneinfo import ZoneInfo

@dg.asset
def fetch_opera_reservations_asset(context: dg.AssetExecutionContext, adls2: ADLS2Resource):
    """
    Fetches reservations directly from the Opera API and uploads JSON to ADLS2 partitioned by date.
    """
    file_system_name = os.environ.get("ADLS2_CONTAINER_NAME")
    date_folder = datetime.now(timezone.utc).strftime("%Y%m%d")
    output_dir = f"dt={date_folder}/batch=raw/"
    output_path = f"{output_dir}reservations.json"

    settings = OperaSettings()
    client = build_opera_client(settings)

    hotel_code = os.getenv("OPERA_HOTEL_CODE", "TBR")
    start_date = os.getenv("START_DATE") or datetime.now(ZoneInfo("America/New_York")).date().isoformat()
    limit = int(os.getenv("LIMIT", "500"))

    context.log.info(f"Fetching Opera reservations for hotel {hotel_code} since {start_date}...")

    reservations = [
        item for item in client.iter_items_created_on_date(
            hotel_code, start_date=start_date, limit=limit
        )
    ]

    adls2.adls2_client.get_file_client(file_system_name, output_path).upload_data(
        json.dumps(reservations, indent=2, ensure_ascii=False), overwrite=True
    )

    context.log.info(f"Uploaded {len(reservations)} reservations to ADLS2 at {output_path}")
    return output_path


@dg.asset
def process_reservations_json_asset(context: dg.AssetExecutionContext, adls2: ADLS2Resource, fetch_opera_reservations_asset):
    """
    Transforms the JSON produced by `fetch_opera_reservations_asset`:
    extracts reservation_id, confirmation_id, cancellation_id, and keeps full reservation data.
    Writes output partitioned by date in JSON Lines format.
    """
    file_system_name = os.environ.get("ADLS2_CONTAINER_NAME")
    input_path = fetch_opera_reservations_asset

    date_folder = datetime.now(timezone.utc).strftime("%Y%m%d")
    batch_folder = "batch_processed"
    output_dir = f"dt={date_folder}/{batch_folder}/"

    output_file_name = "part-000.json"
    manifest_file_name = "manifest.json"
    success_file_name = "_SUCCESS"

    # Read JSON from ADLS2
    file_client = adls2.adls2_client.get_file_client(file_system_name, input_path)
    content = file_client.download_file().readall().decode("utf-8")
    reservations = json.loads(content)

    # Transform into JSON Lines
    result_lines = [
        json.dumps({
            "reservation_id": ids.get("Reservation"),
            "confirmation_id": ids.get("Confirmation"),
            "cancellation_id": ids.get("Cancellation"),
            "data": item
        })
        for item in reservations
        if (ids := {e["type"]: e["id"] for e in item.get("reservationIdList", [])})
    ]

    output_json = "\n".join(result_lines)

    # Upload output files
    adls2.adls2_client.get_file_client(file_system_name, f"{output_dir}{output_file_name}")\
        .upload_data(output_json, overwrite=True)

    manifest_data = {
        "file_names": [output_file_name],
        "run_id": context.run_id,
        "row_count": len(result_lines),
        "time_of_run": datetime.now(timezone.utc).isoformat()
    }
    adls2.adls2_client.get_file_client(file_system_name, f"{output_dir}{manifest_file_name}")\
        .upload_data(json.dumps(manifest_data, indent=2), overwrite=True)

    adls2.adls2_client.get_file_client(file_system_name, f"{output_dir}{success_file_name}")\
        .upload_data("SUCCESS", overwrite=True)

    context.log.info(f"Processed {len(result_lines)} records.")
    return f"{len(result_lines)} records processed successfully."

```



```python
import json
import pandas as pd
from dagster_azure.adls2 import ADLS2Resource, ADLS2SASToken

import dagster as dg

@dg.asset
def extract_json_keys(adls2: ADLS2Resource):
    # ADLS configuration
    storage_account_name = "bocaoperadatalakedev"
    file_system_name = "hotel-reservations"

    # Input and output file definitions
    input_path = "boca.json"
    output_file_name = "part-000.json"
    date_folder = "20251020"
    batch_folder = "batch_test"
    output_path = f"{date_folder}/{batch_folder}/{output_file_name}"

    # Read JSON file from ADLS
    file_client = adls2.adls2_client.get_file_client(file_system_name, input_path)
    downloaded = file_client.download_file()
    content = downloaded.readall().decode("utf-8")

    # Parse JSON and extract root keys
    json_data = json.loads(content)
    keys_list = list(json_data.keys())

    # Create new JSON containing only the keys
    output_json = json.dumps({"keys": keys_list}, indent=4)

    # Upload result to ADLS
    output_client = adls2.adls2_client.get_file_client(file_system_name, output_path)
    output_client.upload_data(output_json, overwrite=True)

    # Return confirmation message
    return f"File '{output_path}' created with {len(keys_list)} keys."
```

```python
import pandas as pd
from dagster_azure.adls2 import ADLS2Resource, ADLS2SASToken

import dagster as dg

@dg.asset
def example_adls2_asset(adls2: ADLS2Resource):

    storage_account_name = "bocaoperadatalakedev"
    sas_token = "sv=2024-11-04&ss=bf&srt=o&sp=rwdlacyx&se=2026-10-19T04:16:35Z&st=2025-10-20T20:01:35Z&spr=https&sig=l6nMtu7faLMQGGaS2fPVEMr%2FJN4lO3jK7ihfm%2FncpX4%3D"
    file_system_name = "hotel-reservations"
    path = "path_test/to/my_dataframe.csv"

    df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["A", "B", "C"]})

    csv_data = df.to_csv(index=False)

    file_client = adls2.adls2_client.get_file_client(
        file_system_name, path
    )
    file_client.upload_data(csv_data, overwrite=True)

```

## 02.03. `jobs.py`
```python
import dagster as dg

car_price_job = dg.define_asset_job(
    name="car_price_job",
    selection=dg.AssetSelection.all()
)
```

## 02.04. `schedule.py`
```python
import dagster as dg
from .jobs import car_price_job

car_price_schedule = dg.ScheduleDefinition(
    job=car_price_job,
    cron_schedule="* * * * *", # every minute
)
```






# XX. Test
```python
!pip install azure-storage-file-datalake pandas

import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient

# Configura tus credenciales
storage_account_name = "bocaoperadatalakedev"
sas_token = "sv=2024-11-04&ss=bf&srt=o&sp=rwdlacyx&se=2026-10-19T04:16:35Z&st=2025-10-20T20:01:35Z&spr=https&sig=l6nMtu7faLMQGGaS2fPVEMr%2FJN4lO3jK7ihfm%2FncpX4%3D"
file_system_name = "hotel-reservations"
path = "path/to/my_dataframe.csv"

# Conectarte a ADLS2
service_client = DataLakeServiceClient(
    account_url=f"https://{storage_account_name}.dfs.core.windows.net",
    credential=sas_token
)

# Crear el DataFrame
df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["A", "B", "C"]})
csv_data = df.to_csv(index=False)

# Subir el archivo
file_system_client = service_client.get_file_system_client(file_system=file_system_name)
file_client = file_system_client.get_file_client(path)
file_client.upload_data(csv_data, overwrite=True)

print("✅ Archivo subido exitosamente a ADLS2")
```

