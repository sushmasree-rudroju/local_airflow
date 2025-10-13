from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def sum_numbers(*args):
    total = 0
    for val in args:
        total += val
        return total
with DAG(
    dag_id="rendering_pythoncode",
    start_date=datetime(2022, 1, 1),
    schedule=None,
    catchup=False,
    render_template_as_native_obj=True) as dag:
    sum_nb = PythonOperator(
        task_id="sum_nb",
        python_callable=sum_numbers,
        op_args="{{ dag_run.conf['numbers'] }}",
)
