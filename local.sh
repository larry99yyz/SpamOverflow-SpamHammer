#!/bin/bash

docker build -t spamoverflow .
docker run -d -p 8080:8080 spamoverflow
