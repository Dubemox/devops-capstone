############ project name...
DevOps Task Manager API.
###########

########### project discription...
Real Word Devops work-flow
##########

########### tools...
Git & GitHub — Source Code Management

Task:

Create a GitHub repository.

Create a simple Python application.

Use branches for development.

Commit and push changes.

Create a README.

Deliverable: A version-controlled application.

Stage 2

Build the application

We will create a small Python FastAPI application with:

/ — Home endpoint

/health — Health check

/users — Return sample user data

Automated tests using pytest

Deliverable: A working application ready for deployment.

Stage 3

Docker — Containerization

Tasks:

Write a Dockerfile.

Build an image.

Run a container.

Map ports.

Create a Docker network.

Use Docker volumes.

Push your image to Docker Hub.

Deliverable: Your application running inside a Docker container.

Stage 4

Jenkins — CI/CD Pipeline

Create a Jenkinsfile with these stages:

Checkout code from GitHub.

Install dependencies.

Run tests.

Build Docker image.

Push image to Docker Hub.

Deploy the application.

Configure a GitHub webhook so a push can trigger the pipeline.

Deliverable: Automated build and deployment pipeline.

Stage 5

Kubernetes — Container Orchestration

Create Kubernetes manifests for:

Deployment

Service

ConfigMap

Secret

Readiness and liveness probes

Replica management

Deliverable: Application running on Minikube with multiple replicas.

Stage 6

Ansible — Configuration Management

Use your CentOS VM as the target server.

Write playbooks to:

Install required packages.

Create a deployment user.

Configure services.

Install Docker where supported.

Start and enable services.

Deploy application configuration.

Deliverable: Server configuration automated using Ansible.

Stage 7

Terraform — Infrastructure as Code

Create infrastructure configuration using:

Providers

Variables

Outputs

Resources

State

count

for_each

First, manage local Docker resources. Later, we can provision cloud infrastructure if you choose.

Deliverable: Reproducible infrastructure configuration.

Stage 8

Vagrant — Virtual Machine Automation

Create a Vagrantfile that:

Starts a Linux VM.

Allocates RAM and CPU.

Configures networking.

Provisions software.

Connects to Ansible.

Deliverable: Repeatable Linux lab environment.

Stage 9

Monitoring & Logging

Introduce Prometheus and Grafana.

Learn to monitor:

Application availability.

CPU and memory usage.

Container health.

Application metrics.

Deliverable: A basic operational dashboard.

Stage 10

Real-world troubleshooting challenges

I will deliberately introduce problems for you to solve:

Docker container exits.

Jenkins build fails.

Kubernetes pod enters CrashLoopBackOff.

ImagePullBackOff.

Service cannot reach a pod.

Terraform state mismatch.

Ansible SSH connection failure.

Application health check fails.

Deliverable: Practical troubleshooting experience.
###########

#############################################
          For learning purpose
#############################################          