from airflow.sdk import dag,task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from pendulum import datetime

@dag(
    dag_id="sensors_dag",   
    start_date=datetime(2023,1,1),
    schedule=None,
    tags=["aws"],
)
def sensors_dag():  
    wait_for_file = S3KeySensor(
        task_id = "wait_for_file",
        aws_conn_id="aws_s3",
        bucket_key="s3://airflow-sushmasree/data_*",
        wildcard_match=True,    
    )

    @task
    def process_file(): 
        print("Processing file...") 

    wait_for_file >> process_file() 

sensors_dag()