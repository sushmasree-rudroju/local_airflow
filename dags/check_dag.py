from airflow.sdk import dag, task
from pendulum import datetime

@dag(
        dag_id="check_dag",
        schedule= "@daily",
        start_date= datetime(2025,1,1),
        description= "This DAG creates a dummy file using bash, checks if it exists using bash, and reads it using python.",
        tags= ["data_engineering"],
        max_consecutive_failed_dag_runs=3
)
def check_dag():

    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy.txt'

    @task.bash
    def check_file():
        return 'test -f /tmp/dummy.txt && echo "File exists!" || echo "File does not exist!"'
    
    @task.python
    def read_file():
        print(open("/tmp/dummy.txt", 'rb').read())

    create_file() >> check_file() >> read_file()

check_dag()