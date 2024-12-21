# Apache Airflow Pipelines Setup and Execution

## Apache Airflow Installation

```sh
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace --set webserverSecretKey=36b035307829251316c51c9991c4e9a0
```

## Pipeline definition

```sh
# It's WA better to use PV of dags folder

kubectl cp pipeline-dag.py airflow-webserver-594c759ccc-7st8g:/opt/airflow/dags -n airflow -c webserver
kubectl cp pipeline-dag.py airflow-scheduler-69867d8f7b-gngdg:/opt/airflow/dags -n airflow -c scheduler
kubectl cp pipeline-dag.py airflow-worker-0:/opt/airflow/dags -n airflow -c worker
```

## UI

```sh
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```
