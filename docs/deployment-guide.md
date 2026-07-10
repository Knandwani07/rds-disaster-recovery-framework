# 🚀 Deployment Guide

Follow these steps to deploy the Disaster Recovery Automation Framework.

## Prerequisites

- AWS Account
- Two AWS Regions:
  - us-east-1
  - us-west-2
- IAM permissions
- Verified email address
- Python 3.12 knowledge
- Basic understanding of Amazon RDS

---

## Deployment Steps

1. Create the Amazon VPC and networking resources.
2. Deploy the Amazon RDS MySQL database.
3. Create the Amazon SNS topic.
4. Create the IAM role for Lambda.
5. Create the customer-managed AWS KMS key.
6. Deploy the Lambda function.
7. Configure Lambda environment variables.
8. Create the EventBridge schedule.
9. Deploy the SSM Automation runbook.
10. Create the CloudWatch Dashboard.
11. Create the CloudWatch Alarm.
12. Perform a manual disaster recovery test.
13. Execute the failover runbook.
14. Verify the restored database.

---

## Verification Checklist

- ✅ RDS database available
- ✅ Snapshot created
- ✅ Snapshot replicated to us-west-2
- ✅ Lambda executed successfully
- ✅ EventBridge schedule enabled
- ✅ CloudWatch dashboard displaying metrics
- ✅ CloudWatch alarm configured
- ✅ SNS notifications received
- ✅ SSM runbook executed successfully
- ✅ Restored database available
