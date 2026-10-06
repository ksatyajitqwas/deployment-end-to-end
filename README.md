# DevOps Platform Projects

A collection of production-grade DevOps projects demonstrating modern platform engineering practices on AWS (EKS-focused).

Each folder is a **standalone project** that can be used independently or as a portfolio piece.

| # | Project | Focus | Key Technologies |
|---|---------|-------|------------------|
| 1 | [GitOps EKS Platform](./project1-gitops-eks-platform) | Full platform with GitOps | Terraform, EKS, ArgoCD, GitLab CI, Prometheus/Grafana |
| 2 | [Zero-Downtime Deployments](./project2-zero-downtime-deployments) | Progressive delivery | Argo Rollouts / Flagger, Prometheus metrics |
| 3 | [Multi-Environment Terraform](./project3-multi-env-terraform) | IaC maturity | Terraform modules, remote state, tfsec/Checkov |
| 4 | [Centralized Observability](./project4-centralized-observability) | Metrics + Logs + Alerts | Prometheus, Grafana, Loki, Alertmanager |
| 5 | [Cost Optimization Automation](./project5-cost-optimization) | FinOps | Lambda, idle resource detection, Slack reporting |
| 6 | [Disaster Recovery](./project6-disaster-recovery) | Reliability | Automated backups, cross-region restore, runbooks |
| 7 | [Secrets Management](./project7-secrets-management) | Security | Vault / AWS Secrets Manager, rotation, CI integration |

## How to use

```bash
# Clone
git clone https://github.com/ksatyajitqwas/deployment-end-to-end.git
cd deployment-end-to-end

# Work on a specific project
cd project1-gitops-eks-platform
```

## Recommended order for learning / demo

1 → 3 → 2 → 4 → 7 → 5 → 6

## Author

Built as a comprehensive DevOps / Platform Engineering portfolio.
