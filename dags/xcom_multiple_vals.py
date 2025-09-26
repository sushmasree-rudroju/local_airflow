from airflow.sdk import dag, task, Context

@dag
def xcom_multiple_vals():

    @task
    def task_a(ti):
        val = { 
                "val_1" :42,
                "val_2" :43,
              }
        ti.xcom_push(key='my_key', value=val)

        
    @task
    def task_b(ti):
        ti_vals = ti.xcom_pull(key='my_key', task_ids='task_a')
        print(f"Pulled values: {ti_vals}") 

    task_a() >> task_b() 

xcom_multiple_vals()