import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
with mlflow.start_run():

    mlflow.log_metric('accuracy', 0.95)
    mlflow.log_param('max_depth', 6)
    mlflow.log_param('n_estimators', 100)

    mlflow.log_artifact(__file__)







