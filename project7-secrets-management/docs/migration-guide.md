# Secrets Migration Guide

## Before
```yaml
# bad — secret in Git or CI variable
env:
  DB_PASSWORD: "supersecret"
```

## After
```yaml
# ExternalSecret pulls from AWS Secrets Manager
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  secretStoreRef:
    name: aws-secrets-manager
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: prod/demo-app/db
        property: password
```
