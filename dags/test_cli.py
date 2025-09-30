from airflow.decorators import task, dag
from airflow.exceptions import AirflowException
from datetime import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False)
def test_cli():
    
    @task
    def my_task(val):
        raise AirflowException()
        print(val)
        return 42
    
    my_task(80)

test_cli()