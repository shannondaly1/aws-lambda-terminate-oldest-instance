import json
import boto3
from datetime import datetime
def lambda_handler(event, context):
    
    oldest_instance_id = ''
    instances_list = []
    client = boto3.client('ec2', region_name='us-east-1')
    response = client.describe_instances()    
    for r in response['Reservations']:
        for i in r['Instances']:
            if i['State']['Code']==16:
                instances_list.append([i['InstanceId'], i['LaunchTime'].strftime('%Y-%m-%dT%H:%M:%SZ')])
                print(i['InstanceId'], i['LaunchTime'])
                
    if instances_list:            
        instances_list.sort(key=lambda x: x[1], reverse=True)
        if instances_list[0]:
            oldest_instance_id = instances_list[0][0]
            response = client.terminate_instances(InstanceIds=[oldest_instance_id])
            
    return {
        'statusCode': 200,
        'body': 'Success'
    }
