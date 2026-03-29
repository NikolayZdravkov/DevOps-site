#!/bin/bash
set -e

kubectl apply -f k8s/namespace.yml

kubectl create secret generic db-secret \
  --namespace devops-site \
  --from-literal=postgres_user=nzadmin \
  --from-literal=db_password=024219 \
  --from-literal=postgres_db=devops_site

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s

kubectl apply -f k8s/postgres/
kubectl apply -f k8s/backend/
kubectl apply -f k8s/frontend/
kubectl apply -f k8s/ingress.yml

echo "Cluster ready at http://localhost"
