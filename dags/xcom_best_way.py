from airflow.sdk import dag, task

@dag
def xcom_best_way():
    #We have 2 tasks, one that pushes a value to XCom and another that pulls it.
    @task
    def task_a():
        val = 42
        return val #by default, the return value is pushed to XCom with key 'return_value'
        
    @task
    def task_b(val: int):
        print(f"Pulled value: {val}") 

    val = task_a() 
    task_b(val)

xcom_best_way()