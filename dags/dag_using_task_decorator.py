from airflow.sdk import dag, task, chain
from pendulum import datetime

@dag(
        dag_id="dag_using_task_decorator",
        schedule= "@daily",
        start_date= datetime (2025,1,1),
        description= "This DAG does...",
        tags= ["team_a","source_a"],
        max_consecutive_failed_dag_runs=3
)
def my_dag():
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
    
    chain(task_a(), [task_b(), task_d()], [task_c(), task_e()])

 
my_dag()