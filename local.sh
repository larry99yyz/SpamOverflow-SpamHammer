#!/bin/bash

docker build -t spamoverflow .
docker run -d -p 5000:5000 spamoverflow
