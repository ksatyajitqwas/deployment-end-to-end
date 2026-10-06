# Project 2: Zero-Downtime Blue-Green / Canary Deployments

> Progressive delivery on EKS with automated rollback.

## Goal

Demonstrate **safe deployments** with automatic rollback when health checks or Prometheus metrics fail.

**Story for interviews:**  
> "We reduced deployment risk dramatically. Canary analysis + automated rollback now happens in under 90 seconds when error rate or latency spikes."

## Approaches Supported

| Tool            | Style              | Best for                  |
|-----------------|--------------------|---------------------------|
| Argo Rollouts   | Blue-Green / Canary| Native Kubernetes feel    |
| Flagger         | Canary + A/B       | Service mesh / Gateway API|

## Key Features

- Automated canary analysis (success rate, latency, custom metrics)
- Automatic rollback on failed analysis
- Manual promotion gates for production
- Integration with Prometheus
- Slack notifications on promotion / rollback

## Directory Structure

```
project2-zero-downtime-deployments/
├── argo-rollouts/          # Rollout CRDs + analysis templates
├── flagger/                # Flagger canary definitions
├── pipelines/              # CI that updates image tags
├── k8s-manifests/          # Sample application
└── docs/
    ├── blue-green.md
    └── canary-analysis.md
```

## Quick Demo Flow

1. Deploy baseline version of the app
2. Update image tag in Git
3. Argo Rollouts / Flagger starts canary
4. Analysis runs against Prometheus metrics
5. Success → promote | Failure → automatic rollback

## Success Metrics to Showcase

- Time to detect bad deployment: < 2 min
- Time to full rollback: < 90 seconds
- Zero user-facing downtime during successful canaries
