#!/bin/bash

PROJECT_ID="intense-plate-429409-f4"

# Enable the Artifact Registry API for your project
gcloud services enable artifactregistry.googleapis.com --project=$PROJECT_ID

# Create an Artifact Registry repository
REPO_NAME="sb-repo"
REPO_DESCRIPTION="Docker repository for StockBuddy scraper"
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=us-central1 \
    --description="$REPO_DESCRIPTION" \
    --project=$PROJECT_ID

# Configure Docker to use the Artifact Registry
gcloud auth configure-docker us-central1-docker.pkg.dev --project=$PROJECT_ID

# Build and tag the Docker image
APP_NAME="test-sb"
docker build --no-cache -t us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$APP_NAME .

# Push the Docker image to the Artifact Registry
docker push us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$APP_NAME

# Deploy the Docker image to Cloud Run
SERVICE_NAME="sb-service"
gcloud run deploy $SERVICE_NAME \
    --image us-central1-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$APP_NAME \
    --region us-central1 \
    --platform managed \
    --memory=32Gi \
    --cpu=8 \
    --timeout=60m \
    --project=$PROJECT_ID
