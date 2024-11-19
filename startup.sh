#! /bin/bash

# build image and recreate container
docker-compose up --build --force-recreate api
