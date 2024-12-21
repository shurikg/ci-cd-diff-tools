# Argo Workflow Pipelines Setup and Execution

## Argo Workflow Installation

```sh
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.6.2/install.yaml

# Configure "simple" access to dashboard
kubectl patch deployment \
    argo-server \
    -n argo \
    --type='json' \
    -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/args", "value": ["server","--auth-mode=server"]}]'

# Add relevant permissions
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default -n argo
```

## Template and Pipeline definition

```sh
kubectl apply -f argo-workflow/echo-template.yaml
kubectl create -f argo-workflow/pipeline-example.yaml
```

## UI

```sh
kubectl -n argo port-forward service/argo-server 2746:2746
```
