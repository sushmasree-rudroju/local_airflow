from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2022, 1, 1), 
     schedule="@once", catchup=False)
def decorator_dag():

    @task(retries=3)
    def start():
        return 'success'
    
    @task.branch
    def choose_task(next_task: str):
        return next_task
    
    @task(retries=1)
    def success():
        print("Success!")

    @task
    def failure():
        print("Failure!")

    choose_task(start()) >> [success(), failure()]

decorator_dag()