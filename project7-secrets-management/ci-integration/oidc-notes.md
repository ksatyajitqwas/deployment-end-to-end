# CI Authentication without long-lived keys

Use GitHub Actions / GitLab OIDC to assume an IAM role that has
`secretsmanager:GetSecretValue` permission only for the required secrets.

No AWS access keys stored in CI variables.
