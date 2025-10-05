from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id='PROCESS_DAG_ID_HOLDER', 
         start_date=datetime(2022, 1, 1), 
         schedule='SCHEDULE_INTERVAL_HOLDER', 
         catchup=False) as dag:
    
    @task
    def extract(filename):
        return filename
    
    @task
    def process(filename):
        return filename
    
    @task
    def send_email(filenmae):
        print(filename)
        return filename
    
    send_email(process(extract("INPUT_HOLDER")))