# 🖼️ Images & Screenshots

This folder contains screenshots captured throughout the implementation of the **AWS Disaster Recovery Automation Framework**. Each document provides a visual representation of an AWS resource or service along with a brief explanation of its role in the disaster recovery workflow.

These screenshots serve as evidence of the successful deployment, configuration, automation, monitoring, and testing of the solution.

---

## 📂 Contents

| File | Description |
|------|-------------|
| `cloudwatch-dashboard.md` | CloudWatch dashboard monitoring Amazon RDS storage, Lambda execution, and overall workflow health. |
| `eventbridge-rule.md` | Amazon EventBridge scheduled rule that automatically triggers the Lambda function for daily snapshot replication. |
| `iam-role.md` | IAM role configured with the permissions required for the Lambda function to access AWS resources. |
| `kms-key.md` | Customer-managed AWS KMS key used to encrypt replicated Amazon RDS snapshots. |
| `lambda-function.md` | AWS Lambda function responsible for snapshot creation, encryption, cross-region replication, and notifications. |
| `primary-rds-database.md` | Primary Amazon RDS MySQL database hosted in the primary AWS Region. |
| `sns-topic.md` | Amazon SNS topic used to deliver disaster recovery and replication notifications. |
| `sns-replication-notification.md` | Email notification confirming successful cross-region snapshot replication. |
| `sns-failover-notification.md` | Email notification confirming successful database restoration after disaster recovery. |
| `ssm-runbook-workflow.md` | AWS Systems Manager Automation workflow illustrating the automated failover process. |

---

## 🎯 Purpose

The screenshots in this folder help demonstrate:

- Deployment of AWS resources
- Automated snapshot replication
- Disaster recovery workflow
- Monitoring and alerting
- Database restoration process
- Security and encryption configuration
- Successful execution of the complete disaster recovery solution

Together, these images provide a visual walkthrough of the project's architecture, automation, and operational workflow.
