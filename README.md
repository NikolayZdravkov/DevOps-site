# DevOps Site

A full-stack web application built as an end-to-end DevOps portfolio project. Developed for learning purposes :3

## Stack

- **Frontend** — Static HTML/CSS/JS served by Nginx
- **Backend** — Python Flask API with Gunicorn
- **Database** — PostgreSQL
- **Containerisation** — Docker + Docker Compose
- **Orchestration** — Kubernetes (Kind for local, AKS for cloud)
- **CI/CD** — GitHub Actions
- **IaC** — Terraform (Azure) (TODO)

## Prerequisites

- Python 3.13+
- Docker & Docker Compose
- kubectl
- Kind
- Task

## Installing Prerequisites

**Kind**
```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.27.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

**Task**
```bash
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b ~/.local/bin
```

## Running locally

### With Python

```bash
cp .env.example .env   # fill in your values
task install
task run
```

### With Docker Compose

```bash
mkdir secrets
echo "yourpassword" > secrets/db_password.txt
docker compose up --build
```

Visit `http://localhost`

### With Kubernetes (Kind)

```bash
task cluster-up
```

Visit `http://localhost`

## Development

```bash
task test    # run tests
task lint    # run linter
```
