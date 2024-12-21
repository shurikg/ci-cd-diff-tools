
# Kestra Pipelines Setup and Execution

## Kestra Installation

```sh
helm repo add kestra https://helm.kestra.io/
helm install kestra kestra/kestra
```

## Template and Pipeline definition

```sh
kubectl apply -f kestra/pipeline.yaml
```

## UI

```sh
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kestra,app.kubernetes.io/instance=kestra,app.kubernetes.io/component=standalone" -o jsonpath="{.items[0].metadata.name}")

kubectl port-forward --namespace default $POD_NAME 8080:8080
```
