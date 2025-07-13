#!/bin/bash
set -e

echo "Starting deployment"

cd ~/personal-website-backend

git pull origin main

docker compose down

docker compose up --build -d

echo "Completed"