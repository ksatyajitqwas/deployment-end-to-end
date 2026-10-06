# Runbook: Restore EKS Cluster from Velero Backup

## Prerequisites
- Target cluster is healthy and Velero is installed
- Backup location (S3) is accessible

## Steps

1. List available backups
   ```bash
   velero backup get
   ```

2. Restore
   ```bash
   velero restore create --from-backup <backup-name>
   ```

3. Validate
   - Check pods are Running
   - Run smoke tests against critical services
   - Verify data integrity for stateful workloads

4. Communicate status to stakeholders
