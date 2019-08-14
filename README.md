# AWS Lambda - Terminate Oldest Instance

This script is designed to be used as a Lambda function in AWS. 
The script will find the oldest EC2 instance in the Region
where the Lambda script is run and then terminates it. Very useful
when dealing with ECS clusters.

Uses the Python 3.7 Runtime in AWS Lambda.

This function can be set on a Schedule by setting up a Cloudwatch Rule.
