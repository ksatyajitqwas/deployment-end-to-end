# Project 3: Multi-Environment Terraform Setup

> IaC maturity beyond "terraform apply once".

## What this demonstrates

- Reusable Terraform **modules**
- Separate **dev / staging / prod** environments
- Remote state in **S3 + DynamoDB locking**
- Policy-as-code with **tfsec** and **Checkov** in CI
- Clear promotion path and least-privilege IAM

## Directory Layout

```
project3-multi-env-terraform/
├── modules/
│   ├── vpc/
│   ├── eks/
│   ├── rds/
│   └── s3/
├── environments/
│   ├── dev/
│   ├── staging/
│   └── prod/
├── policies/
└── ci/
```

## Remote State Pattern

```hcl
terraform {
  backend "s3" {
    bucket         = "company-tf-state"
    key            = "project3/prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## CI Policy Checks

```bash
tfsec .
checkov -d .
terraform fmt -check
terraform validate
```

## Key Principles Shown

1. Modules are the unit of reuse — environments only compose modules
2. State is isolated per environment
3. No credentials in code — use OIDC / assumed roles
4. Plan is always reviewed before apply in higher environments
