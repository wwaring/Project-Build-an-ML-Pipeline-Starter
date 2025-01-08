import mlflow

# Set tracking URI to W&B
mlflow.set_tracking_uri("wandb")

# List all experiments
experiments = mlflow.search_experiments()

# Find the experiment named 'nyc_airbnb'
for experiment in experiments:
    if experiment.name == "nyc_airbnb":
        print(f"Experiment Name: {experiment.name}")
        print(f"Experiment ID: {experiment.experiment_id}")
        break
else:
    print("Experiment 'nyc_airbnb' not found.")
