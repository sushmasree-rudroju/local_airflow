from airflow.sdk import task, DAG
from pendulum import datetime

with DAG(
        dag_id="dag_using_context_manager",
        schedule= "@daily",
        start_date= datetime (2025,1,1),
        description= "This DAG does...",
        tags= ["team_a","source_a"],
        max_consecutive_failed_dag_runs=3
):
    @task
    def task_a():
        print("Hello from task A of context manager DAG!")

    @task
    def task_a():
        print("Hello from task A of my DAG!")
    
    @task
    def task_b():
        print("Hello from task B of my DAG!")
    
    @task
    def task_c():
        print("Hello from task C of my DAG!")
    
    @task
    def task_d():
        print("Hello from task D of my DAG!")

    @task
    def task_e():
        print("Hello from task E of my DAG!") 
        
    a = task_a()
    a >> task_b() >> task_c()
    a >> task_d() >> task_e()
