# 📘 DR Failover Runbook

This folder contains the AWS Systems Manager (SSM) Automation runbook used to automate disaster recovery for the Amazon RDS database.

The runbook performs the following tasks:

- Restores a new Amazon RDS instance from a replicated snapshot.
- Waits until the restored database becomes available.
- Sends an Amazon SNS notification confirming successful failover.

---

## 📂 Files

| File | Description |
|------|-------------|
| `dr-failover-runbook.json` | SSM Automation document that restores the database and sends a completion notification. |

---

## 🔍 How It Works

### 1. Restore the Database
The runbook restores a new Amazon RDS instance from the specified replicated snapshot in the disaster recovery region.

### 2. Wait for Availability
It continuously checks the database status until the restored instance becomes **Available**, ensuring it is ready for use.

### 3. Send Notification
After the database is successfully restored, the runbook publishes an Amazon SNS notification to inform administrators that the failover has completed.

---


## 🚀 Workflow

```
Replicated Snapshot
        │
        ▼
Restore RDS Database
        │
        ▼
Wait Until Available
        │
        ▼
Send SNS Notification
```

---

## ☁️ AWS Services Used

- AWS Systems Manager Automation
- Amazon RDS
- Amazon SNS
