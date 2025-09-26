from airflow.sdk import dag, task, Context

@dag
def xcom_dag():
    #to demonstrate XComs, we need to access task instance object from context of the task
    #Conetct is a dictionary that contains information about the task instance, dag run, etc.
    #We have 2 tasks, one that pushes a value to XCom and another that pulls it.
    @task
    def task_a(**context: Context):
        val = 42
        context['ti'].xcom_push(key='my_key', value=val)
        
    @task
    def task_b(**context: Context):
        val = context['ti'].xcom_pull(key='my_key', task_ids='task_a')
        print(f"Pulled value: {val}") 

    task_a() >> task_b()

xcom_dag()