#!/usr/bin/env bash

# Execute this to update/create a fresh new cloudformation stack
aws --region sa-east-1 cloudformation deploy --stack-name TEMPLATE-CHANGE --template-file pipeline.json --capabilities CAPABILITY_IAM
