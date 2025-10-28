from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import HttpOperator
from datetime import datetime
import json

with DAG(
    dag_id='sharedata_decorators_classicOperators',
    start_date=datetime(2022, 1, 1),
    schedule='@once'
) as dag:
    
    #create a connection https://api.publicapis.org/
    get_api_data = HttpOperator(
        task_id='get_api_data',
        endpoint='/entries',
        do_xcom_push=True,
        http_conn_id='api',
        method='GET'
    )

    @task
    def parse_results(api_results):
        print(json.loads(api_results))

    parse_results(api_results=get_api_data.output)