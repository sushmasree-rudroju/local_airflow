from airflow.sdk import dag,task, Variable

@dag
def variable_dag():

    @task
    def print_my_var():
        print(Variable.get("api", deserialize_json=True))
        
    print_my_var()

variable_dag()

