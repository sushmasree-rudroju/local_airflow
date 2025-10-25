from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="share_data_dag",
    schedule="@once",
    start_date=datetime(2022, 1, 1),
) as dag:

    @task
    def t1():
        return 42
        
    @task
    def t2(value: int):
        print(value)

    t2(t1())