import mlflow

mlflow.set_tracking_uri("wandb")
experiments = mlflow.search_experiments()
print([exp.name for exp in experiments])
