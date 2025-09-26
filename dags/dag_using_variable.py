from airflow.sdk import task, DAG
from pendulum import datetime

d = DAG(
        dag_id="dag_using_variable",
        schedule= "@daily",
        start_date= datetime (2025,1,1),
        description= "This DAG does...",
        tags= ["team_a","source_a"],
        max_consecutive_failed_dag_runs=3
)

@task(dag=d)
def task_a():
    print("Hello from task A using variable DAG!")

@task(dag=d)
def task_b():
    print("Hello from task B using variable DAG!")

task_b() << task_a()