# DevOps Platform Engineering Portfolio

> Production-grade projects that demonstrate the skills companies actually hire for:  
> **GitOps · Progressive Delivery · Multi-env IaC · Observability · FinOps · Reliability · Secrets**

This repository is intentionally structured as **seven independent projects**.  
Each one is self-contained and designed to be discussed in interviews as a concrete example of real platform engineering work.

---

## Why this portfolio stands out

Most candidates show "I can write a Terraform file" or "I used Kubernetes once".  
This portfolio shows end-to-end ownership of the problems platform teams solve every day:

| Skill Area              | What you can confidently talk about                              |
|-------------------------|------------------------------------------------------------------|
| Platform / GitOps       | Full EKS platform with ArgoCD, CI, monitoring & promotion paths  |
| Progressive Delivery    | Canary + automated rollback with real metrics-driven decisions   |
| Infrastructure as Code  | Multi-env modules, remote state, policy-as-code (tfsec/Checkov)  |
| Observability           | Prometheus + Grafana + Loki + Alertmanager built from scratch   |
| Cost / FinOps           | Automated discovery of waste + quantified savings reporting      |
| Reliability Engineering | Backup automation + tested DR drills + runbooks                  |
| Security                | Secrets migration, rotation, OIDC, zero secrets in Git           |

---

## Projects at a glance

| # | Project | One-line pitch | Interview talking points |
|---|---------|----------------|--------------------------|
| **1** | [GitOps EKS Platform](./project1-gitops-eks-platform) | Full platform: Terraform → GitLab CI → ArgoCD → EKS + monitoring | Deploy frequency, lead time, MTTR, automated promotion |
| **2** | [Zero-Downtime Deployments](./project2-zero-downtime-deployments) | Canary / blue-green with automated rollback on failed metrics | "Rollback in < 90s when error rate spikes" |
| **3** | [Multi-Environment Terraform](./project3-multi-env-terraform) | Reusable modules + remote state + policy checks | IaC maturity beyond "terraform apply once" |
| **4** | [Centralized Observability](./project4-centralized-observability) | Prometheus + Grafana + Loki + Alertmanager + SLOs | Built observability from scratch, not just used it |
| **5** | [Cost Optimization Automation](./project5-cost-optimization) | Lambda that finds idle resources and reports savings | Quantified impact: "$X/month identified" |
| **6** | [Disaster Recovery](./project6-disaster-recovery) | Automated backups + cross-region restore drills | RTO/RPO targets + tested runbooks |
| **7** | [Secrets Management](./project7-secrets-management) | Migration to Secrets Manager / Vault + rotation | No secrets in Git, OIDC, automatic rotation |

---

## Recommended discussion order in interviews

1. **Start with Project 1** (GitOps platform) — shows breadth  
2. **Dive into Project 2 or 3** depending on the role (delivery vs IaC)  
3. **Highlight Project 4 or 5** if they care about operations / cost  
4. **Close with Project 6 or 7** to show reliability & security maturity

---

## How to explore

```bash
git clone https://github.com/ksatyajitqwas/deployment-end-to-end.git
cd deployment-end-to-end

# Pick any project
cd project1-gitops-eks-platform
cat README.md
```

Every project contains:
- Clear README with architecture notes and interview-ready stories
- Realistic folder structure (Terraform, Helm, CI, runbooks, etc.)
- Sample manifests / code that demonstrate the concept

---

## Tech stack covered

`Terraform` · `AWS EKS` · `ArgoCD` · `Argo Rollouts` · `GitLab CI` · `Prometheus` · `Grafana` · `Loki` · `Alertmanager` · `Velero` · `AWS Secrets Manager` · `External Secrets` · `Lambda` · `S3` · `DynamoDB` · `tfsec` · `Checkov` · `OIDC`

---

## Note on scope

These are **portfolio / interview demonstration projects**.  
They intentionally focus on architecture, patterns, and storytelling rather than being fully production-hardened end-to-end systems.  
The goal is to give interviewers concrete examples they can dig into — not a single monolithic application.

---

**Built for DevOps / Platform Engineering / SRE interviews.**
