#!/usr/bin/env python3
import boto3
import config
import subs

client = boto3.client('dynamodb')

resp = client.create_table(
    TableName=config.DDB_TABLE,
    AttributeDefinitions=[
        {
            'AttributeName': 'instanceid',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'instanceid',
            'KeyType': 'HASH'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
    Tags=subs.get_tags()
)

print(resp)
