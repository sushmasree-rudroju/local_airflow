from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

def days_to_now(data_interval_start, starting_date):
    return (data_interval_start - starting_date).days


with DAG(dag_id='template_create_macro', 
         start_date=datetime(2022, 1, 1), 
         schedule='@daily', 
         catchup=False,
         template_searchpath=['include'],
         user_defined_macros={'days_to_now': days_to_now}) as dag:
    
    run_this = BashOperator(
        task_id='run_this',
        bash_command='echo days since {{dag.start_date}} is {{days_to_now(data_interval_start, dag.start_date)}}'
    )