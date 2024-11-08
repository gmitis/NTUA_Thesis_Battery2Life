#!/bin/bash

# create necessary log files, essential before startup cause we map them with docker volumes
touch mosquitto-client/mosquitto-client.log

touch battery2life/app.log

# create env file then add the variables
touch battery2life/.env.dev 
