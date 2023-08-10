#!/usr/bin/env python3
import boto3
import config
import subs

client = boto3.client('ec2')

resp = client.create_key_pair(
    KeyName=config.KEY_NAME,
    TagSpecifications=[{'ResourceType': 'key-pair', 'Tags': subs.get_tags()}]
)
key = resp['KeyMaterial']

subs.write_file(config.KEY_FILE, key)

print(resp)
