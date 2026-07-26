# 🚨 AWS RDS Disaster Recovery Automation Framework

## 📖 About this Project

The **AWS Disaster Recovery Automation Framework** is a cloud-based disaster recovery solution that automates backup, cross-region replication, monitoring, and failover for Amazon RDS MySQL databases. Built using an event-driven architecture, the project leverages AWS services such as Lambda, EventBridge, KMS, SNS, CloudWatch, and Systems Manager Automation to reduce manual intervention and improve recovery readiness.

The solution creates encrypted database snapshots, replicates them to a secondary AWS Region, continuously monitors the replication workflow, and enables automated database restoration during disaster recovery scenarios. By automating critical recovery operations, the framework minimizes Recovery Time Objective (RTO), improves operational reliability, and helps organizations maintain business continuity.

---

## 🎯 Project Objectives

- Automate Amazon RDS snapshot creation.
- Replicate encrypted snapshots across AWS Regions.
- Secure backups using AWS Key Management Service (KMS).
- Schedule daily replication using Amazon EventBridge.
- Monitor the disaster recovery workflow with Amazon CloudWatch.
- Send automated notifications using Amazon SNS.
- Enable one-click database restoration using AWS Systems Manager Automation.
- Reduce manual effort during disaster recovery operations.
- Improve disaster recovery readiness through automation and monitoring.
- Demonstrate AWS best practices for backup, encryption, monitoring, and recovery.

---

## 🛠️ Technologies Used

| Service | Purpose |
|----------|---------|
| Amazon VPC | Network isolation |
| Amazon RDS (MySQL) | Primary database |
| AWS Lambda | Snapshot automation |
| Amazon EventBridge | Scheduled execution |
| AWS KMS | Snapshot encryption |
| Amazon SNS | Email notifications |
| Amazon CloudWatch | Monitoring & alarms |
| AWS IAM | Access management |
| AWS Systems Manager Automation | Automated failover |
| Python 3.12 | Lambda runtime |
| JSON | SSM Automation document |

---

## 📂 Project Structure

```text
aws-disaster-recovery-automation-framework/
│
├── architecture/
│   ├── architecture-overview.md
│   └── README.md
│
├── docs/
│   ├── execution-workflow.md
│   ├── deployment-guide.md
│   ├── cleanup-guide.md
│   └── README.md
│
├── images/
│   ├── README.md
│   ├── cloudwatch-dashboard.md
│   ├── eventbridge-rule.md
│   ├── iam-role.md
│   ├── kms-key.md
│   ├── lambda-function.md
│   ├── primary-rds-database.md
│   ├── sns-topic.md
│   ├── sns-replication-notification.md
│   ├── sns-failover-notification.md
│   └── ssm-runbook-workflow.md
│
├── lambda/
│   ├── dr-snapshot-replicator.py
│   └── README.md
│
├── ssm/
│   ├── dr-failover-runbook.json
│   └── README.md
│
├── .gitignore
├── LICENSE
└── README.md
```
---

## 📄 File Description

| File / Folder | Description |
|---------------|-------------|
| **architecture/** | Contains the project architecture overview and design documentation. |
| **docs/** | Includes deployment, execution workflow, and cleanup documentation for the project. |
| **images/** | Contains screenshots of AWS resources and services with explanations demonstrating each stage of the disaster recovery workflow. |
| **lambda/** | Contains the AWS Lambda source code and documentation for automated snapshot replication. |
| **ssm/** | Contains the AWS Systems Manager Automation runbook and its documentation for automated database failover. |
| **.gitignore** | Specifies files and directories that Git should ignore. |
| **LICENSE** | Contains the MIT License governing the use and distribution of this project. |
| **README.md** | Main project documentation, including architecture, setup, implementation, and usage instructions. |

## 📋 Prerequisites

Before deploying this project, ensure you have:

- AWS Account
- Basic knowledge of AWS services
- Familiarity with Amazon RDS
- Understanding of VPC networking
- Basic Python knowledge
- Knowledge of IAM Roles and Policies
- Basic understanding of JSON
- Access to two AWS Regions:
  - **us-east-1 (Primary)**
  - **us-west-2 (Disaster Recovery)**
- Verified email address for Amazon SNS notifications
- AWS Management Console access with sufficient IAM permissions

---

## 📚 Concepts Covered

This project demonstrates practical implementation of the following AWS concepts:

- Disaster Recovery (DR)
- Cross-Region Backup Strategy
- Recovery Time Objective (RTO)
- Recovery Point Objective (RPO)
- Event-Driven Architecture
- AWS Lambda Automation
- EventBridge Scheduling
- Systems Manager Automation Runbooks
- Secure Database Deployment
- Infrastructure Monitoring
- Business Continuity Planning
- AWS Security Best Practices

---

## 🤝 Let's Connect

- 💼 **LinkedIn:** https://www.linkedin.com/in/khushi-nandwani/
- 💻 **GitHub:** https://github.com/Knandwani07
- 📬 **Substack:** https://substack.com/@khushinandwani07
- ✍️ **Dev Community:** https://dev.to/khushi_nandwani07
- 📝 **Medium:** https://medium.com/@khushinandwanii
- 🌐 **Portfolio:** https://main.d1n4wt6uo5bfx6.amplifyapp.com/

---

⭐ **If you found this project helpful, consider giving it a star!**


---
