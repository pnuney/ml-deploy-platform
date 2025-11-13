# ML Deployment Platform

A production style machine learning inference platform built with FastAPI, Docker, AWS ECS Fargate, and Terraform. The project packages a prediction API into a container, pushes it to ECR, and deploys it behind an Application Load Balancer for scalable real time inference.

## Features

- Containerized FastAPI prediction service built for cloud native deployment  
- ECS Fargate task running the API in a fully managed serverless compute environment  
- Public Application Load Balancer forwarding HTTP traffic to the inference service  
- Health check monitoring on the `/health` endpoint for high availability  
- CloudWatch logging for application level visibility  
- Terraform configuration that provisions all cloud resources automatically  
- Fully isolated VPC with subnets, route tables, Internet gateway, and security groups  

## Architecture

Client
|
v
Application Load Balancer
|
v
Target Group (HTTP 8080)
|
v
ECS Fargate Task
|
v
FastAPI Inference Service


## Deployment Overview

### 1. Build and containerize the application

The FastAPI app is packaged into a Docker image built for linux/amd64 for Fargate compatibility.

### 2. Push the image to ECR

The image is tagged and pushed to an Amazon Elastic Container Registry repository.

### 3. Apply Terraform infrastructure

Terraform provisions:

- VPC  
- Public subnets  
- Internet gateway  
- Security groups  
- Application Load Balancer  
- Target group with health checks  
- ECS cluster  
- Task definition  
- ECS service running the container  

### 4. Access the deployed API

Once the ECS service registers a healthy target, the API is available at:

http://<alb_dns_name>/health
http://<alb_dns_name>/predict


## Local Development

### Run FastAPI locally

pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8080

### Run Docker locally

docker build -t ml-deploy-platform .
docker run -p 8080:8080 ml-deploy-platform

## Terraform Deployment

From the `infra` directory:

terraform init
terraform apply

Terraform outputs the public ALB DNS name after deployment.

## Project Structure

ml-deploy-platform/
app/
main.py
model_utils.py
requirements.txt
models/
infra/
main.tf
variables.tf
outputs.tf
Dockerfile
.dockerignore
README.md


## About This Project

This project demonstrates the full lifecycle of deploying an ML inference service to production style infrastructure. It includes containerization, image management, load balanced ECS deployment, automated IaC, and real time request handling. It can be extended with model loading from S3, HTTPS via ACM, autoscaling policies, and CI CD integration.
