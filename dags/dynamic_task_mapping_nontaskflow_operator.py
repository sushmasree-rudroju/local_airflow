from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from datetime import datetime
import random

with DAG (
    dag_id = "dynamic_task_mapping_nontaskflow_operator",
    start_date = datetime(2022,1,1),
    schedule="@daily",
    catchup= False
) as dag:
    
    @task
    def get_files():
        return ["file_{nb}" for nb in range(random.randint(3,5))]
    
    @task
    def download_files(folder: str,file: str):
        return f"ls {folder}/{file}; exit 0"   
    
    files = download_files.partial(folder='/usr/local').expand(file=get_files())

    BashOperator.partial(task_id="ls_file").expand(bash_command=files)

