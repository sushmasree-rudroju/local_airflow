import os
import shutil
import json
import fileinput

TEMPLATE_FILE = 'include/templates/process_file.py' 

for filename in os.listdir('include/data'): 
    if filename.endswith('.json'):
        config = json.load(open(f"include/data/{filename}"))
        current_dir = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(current_dir, '..', '..'))
        new_dag_file = f"dags/process_{config['dag_id']}_dag.py" 
        shutil.copyfile(TEMPLATE_FILE, new_dag_file)
        for line in fileinput.input(new_dag_file, inplace=True):
            line = line.replace('PROCESS_DAG_ID_HOLDER', config['dag_id'])
            line = line.replace('SCHEDULE_INTERVAL_HOLDER', config['schedule_interval'])
            line = line.replace('INPUT_HOLDER', config['input'])
            print(line, end='') 
            