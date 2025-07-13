#!/bin/bash
set -e

echo "Starting deployment"

docker compose down

docker compose up --build -d

echo "Completed"