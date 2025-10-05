from airflow import DAG
from airflow.sdk import task
from pendulum import datetime

def create_dag(filename):
    with DAG(f'process_{filename}',
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
        def send_email(filename):
            print(filename)
            return filename

        send_email(process(extract(filename)))

    return dag

for file in ("fileA.csv", "fileB.csv", "fileC.csv", "fileD.csv"):
    globals()[f'dag_{file}'] = create_dag(file)