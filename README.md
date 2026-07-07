# 🚨 AWS RDS Disaster Recovery Automation Framework

> **An event-driven, cross-region disaster recovery solution for Amazon RDS using AWS Lambda, EventBridge, KMS, SNS, CloudWatch, and AWS Systems Manager Automation.**

---

## 📌 Overview

Disaster recovery is a critical part of any cloud architecture. While automated backups help protect data, recovering quickly from a regional outage often requires additional automation.

This project demonstrates how to build a fully automated disaster recovery workflow for an Amazon RDS MySQL database. It uses AWS services to create scheduled snapshots, replicate them securely to another AWS Region, monitor the entire workflow, and restore the database on demand during a disaster.

The solution minimizes manual intervention, improves recovery time, and provides continuous visibility into the disaster recovery process.

---

## ✨ Features

- Automated daily RDS snapshot creation
- Cross-region encrypted snapshot replication
- Customer-managed AWS KMS encryption
- Event-driven automation with Amazon EventBridge
- Email notifications using Amazon SNS
- CloudWatch dashboard and alarms
- Automated database recovery using SSM Automation
- Disaster recovery testing workflow
- Complete AWS resource cleanup guide

---

## 🏗️ Architecture

The solution consists of two AWS Regions.

### Primary Region (us-east-1)

- Amazon VPC
- Amazon RDS MySQL
- AWS Lambda
- Amazon EventBridge
- Amazon SNS
- Amazon CloudWatch

### Disaster Recovery Region (us-west-2)

- Encrypted RDS Snapshots
- AWS KMS
- AWS Systems Manager Automation
- Restored Amazon RDS Instance
- Amazon SNS

---

## 🔄 Workflow

```text
Amazon RDS
      │
      ▼
Lambda creates snapshot
      │
      ▼
Snapshot encrypted using KMS
      │
      ▼
Cross-region snapshot replication
      │
      ▼
SNS notification
      │
      ▼
CloudWatch monitoring
      │
      ▼
Disaster occurs
      │
      ▼
SSM Automation Runbook
      │
      ▼
Restore Amazon RDS
```

---

## 🛠️ AWS Services Used

- Amazon VPC
- Amazon RDS
- AWS Lambda
- Amazon EventBridge
- AWS KMS
- Amazon SNS
- Amazon CloudWatch
- AWS IAM
- AWS Systems Manager Automation

---

## 📂 Project Structure

```text
rds-disaster-recovery-framework/
│
├── lambda/
│   └── snapshot-replicator.py
│
├── ssm/
│   └── failover-runbook.json
│
├── diagrams/
│   └── architecture.png
│
├── screenshots/
│
├── README.md
```

---

## 🎯 Learning Objectives

This project demonstrates how to:

- Build a disaster recovery architecture on AWS
- Automate RDS snapshot replication
- Encrypt snapshots using AWS KMS
- Schedule automation with EventBridge
- Monitor infrastructure using CloudWatch
- Send alerts using SNS
- Perform automated database recovery
- Validate disaster recovery procedures

---

## 🚀 Technologies

- Python 3.12
- AWS Lambda
- Amazon RDS
- AWS Systems Manager
- Amazon EventBridge
- Amazon CloudWatch
- Amazon SNS
- AWS IAM
- AWS KMS

---

## 📈 Future Enhancements

- Terraform deployment
- AWS Backup integration
- Aurora Global Database
- Route 53 automatic failover
- Step Functions orchestration
- Slack and Microsoft Teams notifications
- Automated DR testing pipeline

---

## 📚 Documentation

The repository includes:

- Complete setup guide
- Step-by-step implementation
- Architecture explanation
- Disaster recovery testing
- Cleanup guide

---

## ⭐ Key Takeaways

- Automating disaster recovery reduces manual effort.
- Cross-region replication improves business continuity.
- Monitoring and alerting increase operational visibility.
- Infrastructure automation improves reliability and consistency.

---

## 🤝 Connect With Me

- 💼 LinkedIn: https://www.linkedin.com/in/khushi-nandwani/
- 💻 GitHub: https://github.com/Knandwani07
- ✍️ Dev Community: https://dev.to/khushi_nandwani07
- 📝 Medium: https://medium.com/@khushinandwanii
- 🌐 Portfolio: https://main.d1n4wt6uo5bfx6.amplifyapp.com/

---

## ⭐ If you found this project helpful, consider giving it a star!
