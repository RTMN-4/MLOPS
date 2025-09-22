import mlflow
from mlflow.tracking import MlflowClient

preprocessing_run_id = "6737348b4f7c44179570081bacb85f38"
preprocessor_path = f"runs:/{preprocessing_run_id}/preprocessor"
preprocessor = mlflow.pyfunc.load_model(preprocessor_path)

