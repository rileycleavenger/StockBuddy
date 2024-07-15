#!/bin/bash

gcloud services enable artifactregistry.googleapis.com
gcloud artifacts repositories create sb-repo --repository-format=docker --location=us-central1 --description="Docker repository for soc-scraper"
gcloud auth configure-docker us-central1-docker.pkg.dev
docker build --no-cache -t us-central1-docker.pkg.dev/gator-path-tracker/sb-repo/test-sb .
docker push us-central1-docker.pkg.dev/gator-path-tracker/sb-repo/test-sb
gcloud run deploy soc-service --image us-central1-docker.pkg.dev/gator-path-tracker/sb-repo/test-sb --region us-central1 --platform managed --memory=32Gi --cpu 8 --timeout=60m