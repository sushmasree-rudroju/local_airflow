from airflow.sdk import dag
from airflow.operators.python import PythonOperator
from pendulum import datetime

def _task_a():
    print("Hello from task A of my DAG!")

@dag(
        schedule= "@daily",
        start_date= datetime (2025,1,1),
        description= "This DAG does...",
        tags= ["team_a","source_a"],
        max_consecutive_failed_dag_runs=3
)
def my_dag():
    task_a = PythonOperator(
        task_id="task_a",
        python_callable= _task_a
    )

my_dag()