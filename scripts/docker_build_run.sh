#!/bin/bash

echo "Bulding docker image"
docker build --tag deposit_service:latest .

if [ $# -eq 0 ];
then
    echo "Starting docker service on port 8000"
    docker run --rm -t -p 8000:8000 deposit_service:latest
else
    echo "Starting docker service on port $1"
    docker run --rm -t -p $1:8000 deposit_service:latest
fi