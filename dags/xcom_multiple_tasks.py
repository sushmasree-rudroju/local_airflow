from airflow.sdk import dag, task, Context

@dag
def xcom_multiple_tasks():

    @task
    def task_a(ti):
        val = 42
        ti.xcom_push(key='my_key', value=val)

    @task
    def task_b(ti):
        val = 43
        ti.xcom_push(key='my_key', value=val)
        
    @task
    def task_c(ti):
        ti_vals = ti.xcom_pull(key='my_key', task_ids=['task_a', 'task_b'])
        print(f"Pulled values: {ti_vals}") 

    task_a() >> task_b() >> task_c()

xcom_multiple_tasks()