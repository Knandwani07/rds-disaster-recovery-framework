# 🏛️ Architecture Diagram

<p align="center">
<img width="100%" height="120%" alt="AWS Disaster Recovery Architecture" src="https://github.com/user-attachments/assets/08e7c591-3886-4fb4-9474-fad1692c71ae" />
</p>

The following architecture illustrates how Amazon RDS snapshots are automatically created, encrypted, replicated across AWS Regions, monitored, and restored during a disaster recovery event.

---

# 🧩 Architecture Components

The solution is divided into five logical layers that work together to provide automated backup, cross-region replication, monitoring, and disaster recovery for Amazon RDS.

---

## 🌎 1. Primary Region Networking (`us-east-1`)

This layer hosts the production infrastructure and provides secure networking for the Amazon RDS database.

| Component | Purpose |
|-----------|---------|
| **Amazon VPC** | Provides an isolated virtual network for the application infrastructure. |
| **Public Subnets** | Host the NAT Gateway to enable secure outbound internet access. |
| **Private Subnets** | Host the Amazon RDS database without exposing it to the public internet. |
| **Internet Gateway** | Allows internet connectivity for public resources. |
| **NAT Gateway** | Enables resources in private subnets to access AWS services and the internet securely. |
| **Route Tables** | Direct private subnet traffic through the NAT Gateway. |

---

## 🗄️ 2. Primary Database Layer

This layer contains the production database that serves as the source for backups and disaster recovery.

| Component | Purpose |
|-----------|---------|
| **Amazon RDS (MySQL)** | Hosts the primary production database with automated backups enabled. |
| **DB Subnet Group** | Places the RDS instance across multiple private subnets for high availability. |
| **Security Group** | Controls inbound and outbound database traffic following least-privilege principles. |

---

## 🔄 3. Replication & Automation Layer

This layer automates snapshot creation, encryption, and cross-region replication.

| Component | Purpose |
|-----------|---------|
| **IAM Role** | Grants Lambda permission to manage RDS snapshots, SNS, CloudWatch, and KMS. |
| **AWS Lambda** | Creates RDS snapshots, encrypts them, and copies them to the disaster recovery region. |
| **Amazon EventBridge** | Triggers the Lambda function automatically on a daily schedule. |
| **AWS KMS** | Encrypts replicated snapshots using a customer-managed encryption key. |

---

## 🛡️ 4. Disaster Recovery Region (`us-west-2`)

This layer stores replicated backups and enables rapid database restoration during a disaster.

| Component | Purpose |
|-----------|---------|
| **Encrypted Replica Snapshot** | Stores encrypted copies of the primary RDS snapshots. |
| **AWS Systems Manager Automation** | Executes the failover runbook to restore the latest replicated snapshot automatically. |
| **Amazon RDS (Restored Instance)** | Restores a new MySQL database instance from the replicated snapshot. |

---

## 📊 5. Monitoring & Alerting Layer

This layer continuously monitors the disaster recovery workflow and notifies administrators of failures.

| Component | Purpose |
|-----------|---------|
| **Amazon CloudWatch Dashboard** | Displays metrics for Amazon RDS and AWS Lambda. |
| **CloudWatch Alarm** | Detects snapshot replication failures and operational issues. |
| **Amazon SNS** | Sends email notifications for replication status, failures, and failover completion. |

---

# 🔄 Disaster Recovery Workflow

```
┌──────────────────────────────┐
│ Primary Region (us-east-1)   │
└──────────────┬───────────────┘
               │
               ▼
      Amazon RDS (MySQL)
               │
               ▼
       Daily Snapshot Created
               │
               ▼
     AWS Lambda Replication
               │
               ▼
      Encrypt using AWS KMS
               │
               ▼
   Cross-Region Snapshot Copy
               │
               ▼
┌──────────────────────────────┐
│ Disaster Recovery Region     │
│       (us-west-2)            │
└──────────────┬───────────────┘
               │
               ▼
     Encrypted Replica Snapshot
               │
               ▼
   SSM Automation Runbook
               │
               ▼
 Restored Amazon RDS Instance
               │
               ▼
 CloudWatch Monitoring & SNS Alerts

```

---

## ☁️ AWS Services in this Architecture

### Networking
- Amazon VPC
- Public & Private Subnets
- Internet Gateway
- NAT Gateway

### Database
- Amazon RDS for MySQL
- DB Subnet Group

### Automation
- AWS Lambda
- Amazon EventBridge
- AWS Systems Manager Automation

### Security
- AWS IAM
- AWS KMS

### Monitoring
- Amazon CloudWatch
- Amazon SNS

---

## ✨ Architecture Highlights

- Automated cross-region disaster recovery
- Encrypted RDS snapshot replication
- Event-driven automation using EventBridge
- Fully automated failover with Systems Manager
- Continuous monitoring with CloudWatch
- Email notifications through Amazon SNS
- Private networking using Amazon VPC
- Secure access using IAM and KMS

---

> **Note:** This architecture is intended for educational and demonstration purposes. In production environments, additional enhancements such as Multi-AZ deployments, AWS Backup, Aurora Global Database, Infrastructure as Code (Terraform or CloudFormation), and least-privilege IAM policies are recommended.
