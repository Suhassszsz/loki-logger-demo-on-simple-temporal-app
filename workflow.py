from activities import fetch_data, process_data
from logger import log_workflow

def run_workflow(workflow_id):
    log_workflow(workflow_id, "Workflow started")
    data = fetch_data(workflow_id)
    result = process_data(workflow_id, data["data"])
    log_workflow(workflow_id, f"Workflow result: {result}")
    log_workflow(workflow_id, "Workflow completed")
