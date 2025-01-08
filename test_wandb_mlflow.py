import os
import wandb
import mlflow

# Ensure W&B project and entity are set
os.environ["WANDB_PROJECT"] = "nyc_airbnb"
os.environ["WANDB_ENTITY"] = "wwaring-n-a"

# Verify connection
print("W&B API Key:", os.environ.get("WANDB_API_KEY"))
print("W&B Project:", os.environ.get("WANDB_PROJECT"))
print("W&B Entity:", os.environ.get("WANDB_ENTITY"))

# Login to W&B
wandb.login()

# Set W&B as the tracking URI
mlflow.set_tracking_uri("wandb")

# Check W&B tracking URI
print("Tracking URI:", mlflow.get_tracking_uri())

# Start a test run and log parameters
with mlflow.start_run(experiment_id="216942217408024993"): 
    mlflow.log_param("test_param", "value")
    mlflow.log_metric("test_metric", 0.95)
print("Run logged successfully.")
