# CI/CD & Approval Gates

This repository uses **GitHub Actions** with production-ready patterns:

| Trigger | What happens |
|---------|--------------|
| **Pull Request** | Validate + Plan (Terraform) / lint / manifest checks. Plan is commented on the PR. |
| **Push to `main`** | Apply / Deploy jobs run **only after** GitHub Environment approval. |
| **workflow_dispatch** | Manual runs with environment selection. |

## How approval gates work

1. Go to the repository **Settings → Environments**
2. Create environments: `dev`, `staging`, `production`
3. For `staging` and especially `production`:
   - Enable **Required reviewers**
   - Add yourself (or the platform team)
   - Optionally restrict to protected branches

When an `apply` / `deploy` job targets `environment: production`, GitHub will pause the workflow and wait for an approved reviewer before continuing.

This is the standard way to implement **manual approval gates** without custom tooling.

## Workflows overview

| Workflow | Path filter | PR | Main (with gate) |
|----------|-------------|----|------------------|
| `project1-gitops-eks.yml` | project1… | validate + plan | apply (env gate) |
| `project2-zero-downtime.yml` | project2… | manifest validate | GitOps hand-off (env gate) |
| `project3-multi-env-terraform.yml` | project3… | validate + plan (all envs) | apply (env gate) |
| `project4-observability.yml` | project4… | Helm/YAML validate | deploy (env gate) |
| `project5-cost-optimization.yml` | project5… | lint + TF validate | deploy (env gate) |
| `project6-disaster-recovery.yml` | project6… | script/runbook check | restore-drill (strong gate) |
| `project7-secrets.yml` | project7… | TF validate + secret scan | apply (env gate) |

## OIDC / AWS authentication (recommended)

All Terraform workflows are ready for **OIDC** (no long-lived keys).

1. Create an IAM OIDC provider for GitHub in your AWS account
2. Create roles trusted by `repo:ksatyajitqwas/deployment-end-to-end:*`
3. Uncomment the `aws-actions/configure-aws-credentials` steps in the workflows
4. Set the correct `role-to-assume` ARNs

## Local testing

```bash
# Act (optional) — run workflows locally
act pull_request -W .github/workflows/project3-multi-env-terraform.yml
```

## Interview talking point

> "Every infrastructure change is planned on the PR, reviewed, and only applied to production after an explicit approval gate using GitHub Environments. No one can push straight to prod."
