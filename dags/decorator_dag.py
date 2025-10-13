from airflow.decorators import dag, task
from datetime import datetime
from airflow.operators.python import get_current_context

@dag(start_date=datetime(2022, 1, 1), 
     schedule="@once", catchup=False)
def decorator_dag():

    @task(retries=3)
    def start(ti=None, ds=None):
        print(f"Data interval start is {ds}")
        print(f"TASK INSTANCE IS {ti}")
        return 'success'
    
    @task.branch
    def choose_task(next_task: str):
        context=get_current_context()
        print(context)
        return next_task
    
    @task(retries=1)
    def success(**context):
        print(context)
        print("Success!")

    @task
    def failure():
        print("Failure!")

    choose_task(start()) >> [success(), failure()]

decorator_dag()