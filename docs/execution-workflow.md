# 🛠️ Execution Workflow

This document provides a high-level overview of the deployment and disaster recovery workflow implemented in this project.

## Workflow Overview

### I. Network Setup
- Create an Amazon VPC in `us-east-1`.
- Configure public and private subnets across two Availability Zones.
- Create and configure a NAT Gateway.
- Update private route tables.

### II. Database Deployment
- Create an Amazon RDS MySQL instance.
- Configure the DB subnet group and security group.
- Enable automated backups.

### III. Notification Setup
- Create an Amazon SNS topic.
- Configure an email subscription for alerts.

### IV. IAM Configuration
- Create an IAM role for AWS Lambda.
- Attach the required AWS managed policies.

### V. Encryption Setup
- Create a customer-managed AWS KMS key in `us-west-2`.
- Save the KMS Key ARN for snapshot encryption.

### VI. Snapshot Automation
- Deploy the AWS Lambda function.
- Configure environment variables.
- Test snapshot creation and replication.

### VII. Scheduling
- Create an Amazon EventBridge rule.
- Schedule daily snapshot replication.

### VIII. Disaster Recovery Automation
- Create the AWS Systems Manager Automation runbook.
- Configure the failover document.

### IX. Monitoring
- Create a CloudWatch Dashboard.
- Add RDS and Lambda metrics.

### X. Alerting
- Create a CloudWatch Alarm.
- Send alerts through Amazon SNS when replication fails.

### XI. Disaster Recovery Testing
- Execute the Lambda function manually.
- Verify snapshot replication.
- Confirm SNS notifications.

### XII. Disaster Recovery Notifications
- Create an SNS topic in the disaster recovery region (`us-west-2`).

### XIII. Execute Failover
- Run the SSM Automation document.
- Restore the replicated snapshot.
- Verify the restored database.
- Confirm the failover notification.

### XIV. Cleanup
- Remove all AWS resources to avoid additional charges.

---

## Workflow Summary

```text
Create VPC
      │
      ▼
Deploy RDS
      │
      ▼
Configure SNS
      │
      ▼
Create IAM Role
      │
      ▼
Create KMS Key
      │
      ▼
Deploy Lambda
      │
      ▼
Schedule with EventBridge
      │
      ▼
Create SSM Runbook
      │
      ▼
Configure Monitoring
      │
      ▼
Test Disaster Recovery
      │
      ▼
Execute Failover
      │
      ▼
Cleanup Resources
```
