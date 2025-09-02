import uuid
from workflow import run_workflow

if __name__ == "__main__":
    workflow_id = str(uuid.uuid4())
    run_workflow(workflow_id)
