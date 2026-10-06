"""
Cost optimization scanner (skeleton).
Finds idle EC2, unattached EBS, unused EIPs.
"""

import boto3
from datetime import datetime, timedelta

ec2 = boto3.client("ec2")

def find_unattached_volumes():
    volumes = ec2.describe_volumes(Filters=[{"Name": "status", "Values": ["available"]}])
    return volumes.get("Volumes", [])

def find_unused_eips():
    addresses = ec2.describe_addresses()
    return [a for a in addresses.get("Addresses", []) if "InstanceId" not in a and "NetworkInterfaceId" not in a]

def find_idle_instances(days=7):
    # Simplified: stopped instances older than N days
    instances = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}]
    )
    # Add logic for launch time / last activity
    return instances

def handler(event, context):
    report = {
        "unattached_volumes": len(find_unattached_volumes()),
        "unused_eips": len(find_unused_eips()),
        "timestamp": datetime.utcnow().isoformat(),
    }
    # Send to Slack / SNS
    print(report)
    return report
