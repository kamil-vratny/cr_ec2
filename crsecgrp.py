#!/usr/bin/env python3
import boto3
import config
import subs

client = boto3.client('ec2')

resp = client.create_security_group(
    GroupName=config.SEC_GRP,
    Description='Learning Desktops security group',
    TagSpecifications=[
        {'ResourceType': 'security-group', 'Tags': subs.get_tags()}]
)
group_id = resp['GroupId']

client.authorize_security_group_ingress(
    GroupId=group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '172.16.0.0/12'}]
        }
    ]
)

subs.write_file(config.SEC_GRP_FILE, group_id)

print(resp)
