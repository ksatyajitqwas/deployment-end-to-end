# Project 1: Full GitOps EKS Platform

> **Flagship Project** — A production-ready, end-to-end GitOps platform on AWS EKS.

## Architecture Overview

```
GitLab CI builds/tests → ECR
GitOps Repo (desired state) ← ArgoCD auto-sync → EKS Cluster
Prometheus + Grafana + Alertmanager → Slack
```

## What this project delivers

- **Terraform** provisions VPC + EKS + IAM + core add-ons
- **GitLab CI** builds, tests, and pushes images
- **ArgoCD** continuously syncs the desired state from Git
- **Prometheus + Grafana** with pre-built dashboards
- **Alertmanager** routes critical alerts to Slack
- Documented **metrics**: deploy frequency, MTTR, rollback time

## Key Metrics (demo targets)

| Metric                  | Target          |
|-------------------------|-----------------|
| Deploy frequency        | Multiple / day  |
| Lead time for changes   | < 30 min        |
| Change failure rate     | < 5%            |
| Mean time to restore    | < 15 min        |
| Automated rollback time | < 2 min         |

## Directory Structure

```
project1-gitops-eks-platform/
├── terraform/
│   ├── modules/
│   │   ├── vpc/
│   │   ├── eks/
│   │   ├── iam/
│   │   └── addons/
│   └── environments/
│       ├── dev/
│       ├── staging/
│       └── prod/
├── argocd/
│   ├── apps/
│   └── projects/
├── ci/
├── monitoring/
└── docs/
    ├── architecture.md
    └── runbook.md
```

## Quick Start

```bash
cd terraform/environments/dev
terraform init && terraform apply

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f argocd/projects/
kubectl apply -f argocd/apps/
```
