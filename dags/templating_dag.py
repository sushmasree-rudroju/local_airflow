'''Data pipeline with one task that checks if we have data in a table at a specific date.
We import SQLExecuteQueryOperator to interact with postgres database.
ds is equivalent to data_interval_start of the current DAG Run'''

from airflow import DAG
from datetime import datetime
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(dag_id='templating_dag', 
         start_date=datetime(2022, 8, 15), 
         schedule='@daily', 
         catchup=False) as dag:
   
    get_data = SQLExecuteQueryOperator(
        task_id='get_data',
        conn_id='postgres_default',
        sql ="SELECT EXISTS (SELECT 1 FROM my_table WHERE date='{{ ds}}')"
    )