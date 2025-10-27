from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG('share_data_classicOperators',
         start_date=datetime(2022, 1, 1),
         schedule='@once',
         catchup=False) as dag:

    start = PythonOperator(
        task_id='start',
        python_callable=lambda: 42
    )

    print = BashOperator(
        task_id='print',
        bash_command= f'echo "value from the previous task: {start.output}"'
    )

    start >> print
    