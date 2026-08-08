# Northwind Logistics Delivery Tracking Service

## Overview

This repository contains a complete DevOps implementation for the Northwind Logistics Delivery Tracking Service.

The project demonstrates:

- Git-based version control workflow
- Automated testing with pytest
- Continuous Integration using GitHub Actions
- Configuration management using Ansible
- Containerisation using Docker
- Container orchestration using Kubernetes

## Repository Structure

.github/workflows/
  ci.yml

ansible/
  playbook.yml

app/
  __main__.py
  service.py
  data.py

k8s/
  deployment.yaml
  service.yaml

tests/
  test_data.py
  test_service.py

Dockerfile
requirements.txt
run.py

## Running Locally

python -m app

or

python run.py

## Running Tests

pytest

## CI Pipeline

The GitHub Actions workflow:

1. Checks out the source code
2. Configures Python
3. Installs dependencies
4. Executes pytest
5. Builds the Docker image

The pipeline runs automatically on pushes and pull requests.

## Docker

Build the container image:

docker build -t northwind-delivery-service .

Run the container:

docker run -p 8000:8000 northwind-delivery-service

## Kubernetes

Deploy the application:

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Verify deployment:

kubectl get deployments
kubectl get pods
kubectl get svc

## Configuration Management

Run the Ansible playbook:

ansible-playbook ansible/playbook.yml

The playbook is idempotent and can be executed repeatedly without creating duplicate resources.

## API Endpoints

GET /
GET /health
GET /deliveries
GET /deliveries/{id}