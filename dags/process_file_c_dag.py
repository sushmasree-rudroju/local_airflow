from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(dag_id='file_c', 
         start_date=datetime(2022, 1, 1), 
         schedule='@daily', 
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
    
    send_email(process(extract("file_c.csv")))