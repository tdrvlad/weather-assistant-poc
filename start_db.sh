#!/bin/bash

# Load environment variables from .env file
set -a  # automatically export all variables
source .env
set +a

# Run the PostgreSQL container
docker run -d \
  -e POSTGRES_DB=$POSTGRES_DB \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -p $POSTGRES_PORT:5432 \
  -v $(pwd)/db_data:/var/lib/postgresql/data \
  postgres
