# Project 5: Cost Optimization Automation

> FinOps automation that finds waste and reports savings.

## Goal

Automatically discover idle / unused resources and surface real dollar savings.

**Interview story:**  
> "Built a Lambda that scans for idle EC2, unattached EBS, unused EIPs and Elastic Load Balancers. In the first month it identified ~$1,800/month in potential savings."

## What it does

1. Scans account(s) for:
   - Stopped / idle EC2 instances
   - Unattached EBS volumes
   - Unassociated Elastic IPs
   - Old snapshots
   - Under-utilized RDS / unused Load Balancers
2. Tags resources with `cost-optimization` labels
3. Sends a daily / weekly report to Slack (or Datadog)
4. Optional: auto-remediation with approval gates

## Directory Structure

```
project5-cost-optimization/
├── lambda/
├── scripts/
├── terraform/
├── reports/
└── docs/
```

## Sample Report Format

```
Cost Optimization Report — 2026-10-06
────────────────────────────────────
Unattached EBS volumes:     12  →  ~$180/month
Idle EC2 (stopped > 7d):     4  →  ~$320/month
Unused Elastic IPs:          3  →   ~$11/month
Old snapshots (> 90d):      28  →  ~$95/month
────────────────────────────────────
Estimated monthly savings:  ~$606
```

## Implementation Notes

- Use AWS Cost Explorer + CloudWatch metrics for utilization
- Prefer event-driven (EventBridge) over pure cron where possible
- Never auto-delete without a dry-run + approval path
