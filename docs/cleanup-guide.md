# 🧹 Cleanup Guide

After testing the disaster recovery workflow, remove all AWS resources to avoid unnecessary charges.

## Delete Resources

### Amazon RDS

- Delete `dr-primary-db`
- Delete `dr-restored-db`
- Delete all snapshots

### AWS Lambda

- Delete `dr-snapshot-replicator`

### Amazon EventBridge

- Delete `dr-daily-snapshot-trigger`

### AWS Systems Manager

- Delete `dr-failover-runbook`

### Amazon CloudWatch

- Delete the dashboard
- Delete the replication failure alarm

### Amazon SNS

- Delete `dr-alerts`
- Delete `dr-alerts-west`

### AWS IAM

- Delete `dr-lambda-role`

### AWS KMS

- Schedule deletion of `dr-kms-key` (optional)

### Networking

Delete:

- NAT Gateway
- Amazon VPC
- Public Subnets
- Private Subnets
- Route Tables
- Internet Gateway
- Network Interfaces (if any)

---

## Final Checklist

Before leaving your AWS account, verify that:

- ✅ No RDS instances remain
- ✅ No snapshots remain
- ✅ Lambda function deleted
- ✅ EventBridge rule removed
- ✅ CloudWatch dashboard removed
- ✅ CloudWatch alarms removed
- ✅ SNS topics removed
- ✅ IAM role removed
- ✅ KMS key scheduled for deletion
- ✅ NAT Gateway deleted
- ✅ VPC deleted

Completing these steps helps prevent unexpected AWS charges.
