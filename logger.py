from loguru import logger
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)

logger.add(LOG_FILE, rotation="1 MB", enqueue=True, backtrace=True, diagnose=True)

def log_workflow(workflow_id: str, message: str):
    logger.info(f"[WorkflowID: {workflow_id}] {message}")
