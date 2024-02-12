#!/bin/bash

echo "INFO : Check if docker running"
if ! docker info > /dev/null 2>&1;
    then
        echo "INFO : This script uses docker, and it isn't running - please start docker and try again!"
        exit 1
    else
        echo "INFO : Docker is running"
fi

echo "INFO : Bulding docker image"
docker build --tag deposit_service:latest .
echo "INFO : Buid complited"

echo "INFO : Run tests"
docker run --rm -t --entrypoint="pytest" deposit_service:latest

if [ $? -eq 0 ];
    then
        echo "INFO : All test passed"
    else
        echo "WORRNING : Some tests wasn't passed"
fi

if [ $# -eq 0 ];
    then
        echo "INFO : Starting docker service on port 8000"
        docker run --rm -d -p 8000:8000 deposit_service:latest
    else
        echo "INFO : Starting docker service on port $1"
        docker run --rm -d -p $1:8000 deposit_service:latest
fi