# Project 7: Secrets Management Overhaul

> Eliminate hardcoded secrets. Rotate automatically. Integrate with CI/CD + Terraform.

## Goal

Move from "secrets in Git / environment variables" to a proper secrets platform.

**Interview story:**  
> "Migrated all application and infrastructure secrets to AWS Secrets Manager + External Secrets Operator. Rotation is automatic, no secrets live in Git or CI variables anymore."

## Approaches Covered

| Solution                | Best for                          |
|-------------------------|-----------------------------------|
| AWS Secrets Manager     | AWS-native, simple rotation       |
| HashiCorp Vault         | Multi-cloud, advanced policies    |
| External Secrets Operator | Kubernetes-native sync          |

## What this project shows

1. Secrets **never** committed to Git
2. Terraform creates secret *containers* (not values)
3. CI/CD authenticates via OIDC / short-lived tokens
4. Applications pull secrets at runtime via CSI / External Secrets
5. Automatic rotation for database credentials, API keys, etc.

## Directory Structure

```
project7-secrets-management/
├── vault/
├── aws-secrets-manager/
├── terraform/
├── ci-integration/
└── docs/
    ├── migration-guide.md
    └── rotation-strategy.md
```

## Migration Pattern

1. Inventory all current secrets
2. Create secret in Secrets Manager / Vault
3. Update application to use External Secrets / CSI driver
4. Remove secret from Git / CI variables
5. Enable rotation
6. Audit access

## Security Benefits

- No long-lived credentials in pipelines
- Fine-grained IAM / Vault policies
- Audit trail of every secret access
- Automatic rotation reduces blast radius
