#!/bin/bash

docker build -t scraper-app .
docker run -p 8080:8080 scraper-app
