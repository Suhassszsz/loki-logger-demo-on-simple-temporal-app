import time
from logger import log_workflow

def fetch_data(workflow_id):
    log_workflow(workflow_id, "Activity: Fetching data")
    time.sleep(1)
    return {"data": [1, 2, 3]}

def process_data(workflow_id, data):
    log_workflow(workflow_id, f"Activity: Processing data {data}")
    time.sleep(1)
    return [x * 2 for x in data]
