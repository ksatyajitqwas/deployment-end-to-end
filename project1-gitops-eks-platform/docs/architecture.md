# Architecture — GitOps EKS Platform

## Design Goals

1. Git as the single source of truth
2. Declarative everything (infra + apps)
3. Automated promotion across environments
4. Observable by default
5. Secure by default (IRSA, least privilege)

## Component Choices

| Layer            | Choice              | Why                                      |
|------------------|---------------------|------------------------------------------|
| IaC              | Terraform           | Mature, AWS provider excellence          |
| Orchestration    | EKS                 | Managed control plane, IRSA support      |
| GitOps           | ArgoCD              | Pull-based, multi-cluster ready          |
| CI               | GitLab CI           | Built-in container registry + runners    |
| Metrics          | Prometheus          | De-facto standard on Kubernetes          |
| Visualization    | Grafana             | Flexible dashboards + alerting           |
| Secrets          | External Secrets + AWS SM / Vault | No secrets in Git             |

## Network Design

- Multi-AZ VPC
- Private subnets for nodes + pods
- Public subnets only for load balancers
- NAT Gateway (or NAT instances for cost savings in non-prod)
- VPC endpoints for ECR, S3, STS to keep traffic private

## Security

- IRSA for all service accounts that need AWS permissions
- Pod Security Standards (restricted) enforced via Kyverno/OPA
- Network policies (Calico or Cilium)
- Image scanning in CI (Trivy)
- No long-lived credentials

## Promotion Flow

```
feature branch → MR → main (dev)
                         ↓
                    staging tag / branch
                         ↓
                    prod (manual approval + ArgoCD sync)
```
