#!/usr/bin/env bash
# ==============================================================================
# CloudPulse AI — Fast-Ship Deployment Script for AWS App Runner
# AWS Hackathon "Zero to Shipped" (Due Oct 2, 2026)
# ==============================================================================

set -euo pipefail

APP_NAME="cloudpulse-ai"
REGION="${AWS_REGION:-us-east-1}"

echo "=========================================================="
echo " Starting Fast-Ship Deployment: ${APP_NAME}"
echo " Region: ${REGION}"
echo "=========================================================="

# 1. Check AWS CLI Authentication (Coding Agent Proof Check)
echo "--> Verifying AWS CLI caller identity..."
aws sts get-caller-identity --output json

ACCOUNT_ID=$(aws sts get-caller-identity --query "Account" --output text)
echo "--> Authenticated to AWS Account: ${ACCOUNT_ID}"

# 2. Check ECR Repository
echo "--> Checking/Creating ECR Repository '${APP_NAME}'..."
aws ecr describe-repositories --repository-names "${APP_NAME}" --region "${REGION}" >/dev/null 2>&1 || \
    aws ecr create-repository --repository-name "${APP_NAME}" --region "${REGION}"

ECR_URI="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${APP_NAME}:latest"

# 3. Docker Login & Build
echo "--> Logging into Amazon ECR..."
aws ecr get-login-password --region "${REGION}" | docker login --username AWS --password-stdin "${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"

echo "--> Building Docker image..."
docker build -t "${APP_NAME}" .
docker tag "${APP_NAME}:latest" "${ECR_URI}"

echo "--> Pushing Docker image to ECR..."
docker push "${ECR_URI}"

echo "=========================================================="
echo " Image pushed successfully: ${ECR_URI}"
echo " To deploy directly to AWS App Runner via Console:"
echo " 1. Go to AWS App Runner Console -> Create Service."
echo " 2. Select 'Container registry' -> 'Amazon ECR'."
echo " 3. Enter container image URI: ${ECR_URI}"
echo " 4. Service name: ${APP_NAME} | Port: 8080"
echo " 5. Deploy service and obtain your live public HTTPS URL!"
echo "=========================================================="
