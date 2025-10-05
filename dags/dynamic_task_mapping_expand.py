from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import random

with DAG (
    dag_id = "dynamic_task_mapping_expand",
    start_date = datetime(2022,1,1),
    schedule="@daily",
    catchup= False
) as dag:
    
    @task
    def get_files():
        return ["file_{nb}" for nb in range(random.randint(3,5))]
    
    @task
    def download_files(file: str):
        print(file)
    
    files = download_files.expand(file=get_files())

