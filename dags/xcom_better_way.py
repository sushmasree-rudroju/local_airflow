from airflow.sdk import dag, task

@dag
def xcom_better_way():
    #We have 2 tasks, one that pushes a value to XCom and another that pulls it.
    @task
    def task_a(ti):
        val = 42
        ti.xcom_push(key='my_key', value=val)
        
    @task
    def task_b(ti):
        ti_val = ti.xcom_pull(key='my_key', task_ids='task_a')
        print(f"Pulled value: {ti_val}") 

    task_a() >> task_b()

xcom_better_way()