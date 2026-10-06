# Project 6: Disaster Recovery & Backup Automation

> Reliability engineering — automated backups + tested restore drills.

## Goal

Prove you can recover from failure, not just deploy happily.

**Interview story:**  
> "We automated EKS etcd + application backups and run a quarterly cross-region restore drill. RTO is under 45 minutes, RPO under 15 minutes for critical services."

## Scope

- Automated EKS (Velero) + RDS snapshots
- Cross-region replication
- Scripted restore drills
- Documented runbooks
- Regularly tested (not "we have backups" theater)

## Directory Structure

```
project6-disaster-recovery/
├── backup-scripts/
├── restore-drills/
├── runbooks/
├── terraform/
└── docs/
```

## Key Components

| Component       | Tool / Approach              |
|-----------------|------------------------------|
| Cluster backup  | Velero                       |
| Database        | RDS automated + manual snaps |
| Object storage  | S3 cross-region replication  |
| Orchestration   | CronJob / EventBridge        |
| Validation      | Automated restore + smoke tests |

## Sample RTO / RPO Targets

| Tier     | RPO     | RTO      |
|----------|---------|----------|
| Critical | 15 min  | 45 min   |
| Standard | 1 hour  | 4 hours  |
| Best-effort | 24h  | 24 hours |
