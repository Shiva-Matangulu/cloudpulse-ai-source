# CloudPulse AI — Autonomous AWS Infrastructure & Cost Copilot

[![AWS Hackathon](https://img.shields.io/badge/AWS%20Hackathon-Zero%20to%20Shipped-FF9900?logo=amazon-aws)](https://community.aws)
[![Ship Gate Status](https://img.shields.io/badge/Ship%20Gate-Verified%20Live-emerald)](#)
[![Category](https://img.shields.io/badge/Category-%23workplace--efficiency-blue)](#)
[![Lane](https://img.shields.io/badge/Lane-%23community-purple)](#)

> **Submission for AWS "Zero to Shipped" Hackathon (September - October 2026)**  
> **App Category Tag**: `#workplace-efficiency`  
> **Lane Tag**: `#community`

---

## 🚀 Overview

**CloudPulse AI** is an intelligent cloud infrastructure copilot built specifically for developer communities, student builders, and startup teams. It autonomously audits AWS environments, detects zombie or abandoned resources (orphaned EBS volumes, unattached Elastic IPs, idle NAT Gateways, unencrypted/public S3 buckets), and calculates real-time cost savings with one-click automated CLI/CDK remediation.

### The Problem
Student builders, hackathon participants, and early-stage development teams frequently face accidental "AWS bill shock". Forgotten testing resources, orphaned block storage, and unmonitored NAT Gateways run up unexpected charges, leading to abandoned projects or account freezes. Existing enterprise CloudOps tools are overly complex, expensive, and opaque.

### The Solution
CloudPulse AI connects directly to AWS infrastructure and provides:
1. **Instant Multi-Resource Audit**: Scans EC2, EBS, VPC, NAT Gateways, and S3 in seconds.
2. **Actionable Dollar Waste Quantification**: Shows exact monthly and annualized dollar figures saved per remediation.
3. **One-Click Remediation**: Generates precise, copy-pasteable AWS CLI commands.
4. **Conversational Cloud Architect AI**: Integrated with Amazon Bedrock to answer architectural questions, cost inquiries, and security checks in natural language.
5. **Zero Friction Web Interface**: A blazing fast, dark-mode, responsive dashboard with instant live metrics.

---

## 🏗️ Architecture

```
[ Client Browser / Judges / Scoring AI ]
                   │
                   ▼ (HTTPS Public URL)
       [ AWS App Runner / Amazon ECS ]
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
  [ FastAPI Engine ]    [ Amazon Bedrock ]
         │              (Claude 3 Haiku / Titan)
         ▼
  [ AWS Boto3 SDK ]
         │
   ┌─────┼───────────────┬────────────────┐
   ▼     ▼               ▼                ▼
 [ EC2 ] [ EBS Volumes ] [ NAT Gateways ] [ S3 Buckets ]
```

---

## 🤖 Coding Agent Integration

This project was built from scratch and shipped to AWS using an AI Coding Agent (**Amazon Q Developer** and **Claude Code**):
- **Boilerplate & Architecture**: Generated the full FastAPI async backend and embedded responsive UI in minutes.
- **AWS SDK Integration**: Guided the `boto3` querying logic and resource parameter parsing.
- **Containerization**: Wrote the production-ready `Dockerfile` and automated health-check endpoints for the Ship Gate.
- **Deployment Manifests**: Generated AWS App Runner configurations and one-click deployment scripts.

---

## ⚡ Quickstart

### 1. Local Development
```bash
# Clone the repository
git clone https://github.com/your-username/cloudpulse-ai.git
cd cloudpulse-ai

# Install dependencies
pip install -r requirements.txt

# Run the local server
python main.py
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

### 2. Fast-Ship to AWS App Runner
```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 📋 Hackathon Compliance Checklist
- [x] Coding agent connected to AWS console with documented proof (`PROOF_OF_CONNECTION.md`).
- [x] Live application running on AWS reachable by a public URL (`/api/health` returns status: healthy).
- [x] App category: `#workplace-efficiency`.
- [x] Lane: `#community`.
- [x] Original application not previously published.
