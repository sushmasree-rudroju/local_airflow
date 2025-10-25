from airflow.models.xcom_arg import XComArg
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from airflow import DAG
from datetime import datetime

dag = DAG(dag_id='xcomarg_dag', start_date=datetime(2022, 1, 1))

op= PythonOperator(
    task_id='op',
    python_callable=lambda: 42,
    dag=dag)
xcom = XComArg(op)
print(op)
xcom = XComArg(op)
print(xcom)
print(xcom['my_key'])
print(op.output)

@task(dag=dag)
def start():
    None
start()
