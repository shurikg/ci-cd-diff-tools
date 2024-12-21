# Tekton Pipelines Setup and Execution

## Install Tekton Pipelines and Dashboard

```sh
kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/release-full.yaml
```

## Align permissions

```sh
kubectl apply --filename permissions.yaml
```

## Task and Pipeline definition

```sh
kubectl apply --filename echo-task.yaml
kubectl apply --filename pipeline-example.yaml
```

## Trigger the pipeline

```sh
kubectl create --filename pipeline-run.yaml
```

## UI

```sh
kubectl port-forward -n tekton-pipelines service/tekton-dashboard 9097:9097
```