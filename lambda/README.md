# 📘 DR Snapshot Replicator

This folder contains the AWS Lambda function responsible for automating Amazon RDS snapshot creation and cross-region replication as part of the disaster recovery workflow.

The function creates a snapshot of the primary database, waits for it to become available, copies it to the disaster recovery region using AWS KMS encryption, and sends an Amazon SNS notification indicating whether the replication was successful or failed.

---

## 📂 Files

| File | Description |
|------|-------------|
| `dr-snapshot-replicator.py` | Python Lambda function that automates RDS snapshot creation, encrypted cross-region replication, and SNS notifications. |

---

## 🔍 How It Works

### 1. Create Snapshot
Creates a manual snapshot of the primary Amazon RDS MySQL database in the primary region (`us-east-1`).

### 2. Wait for Completion
Waits until the snapshot status changes to **Available** before proceeding.

### 3. Replicate Snapshot
Copies the snapshot to the disaster recovery region (`us-west-2`) using a customer-managed AWS KMS key for encryption.

### 4. Send Notification
Publishes an Amazon SNS notification indicating whether the replication completed successfully or failed.

---

## 🚀 Workflow

```text
Amazon RDS
     │
     ▼
Create Snapshot
     │
     ▼
Wait Until Available
     │
     ▼
Encrypt with AWS KMS
     │
     ▼
Copy to us-west-2
     │
     ▼
Send SNS Notification
```

---
## ☁️ AWS Services Used

- AWS Lambda
- Amazon RDS
- AWS KMS
- Amazon SNS
- Amazon CloudWatch Logs
