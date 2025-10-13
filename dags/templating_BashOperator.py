from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='templating_BashOperator', 
         start_date=datetime(2022, 1, 1), 
         schedule='@daily', 
         catchup=False,
         template_searchpath=['include']) as dag:
    
    run_this = BashOperator(
        task_id='run_this',
        bash_command='scripts/script.sh'
    )