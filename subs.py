import csv
import boto3
import secrets
import string
import config
import random


def read_csv():
    file = open(config.DATA_FILE, 'r', encoding='utf-8')
    csvfile = csv.reader(file, delimiter=';')
    data = []
    for row in csvfile:
        if 'USERNAME' in row:
            continue
        data.append(row)
    file.close
    return data


def read_file(filename):
    file = open(filename, 'r', encoding='utf-8')
    data = file.read()
    file.close
    return data


def read_whole_file(filename):
    file = open(filename, 'r', encoding='utf-8')
    data = file.readlines()
    data = ''.join(data)
    file.close
    return data


def write_file(filename, data):
    file = open(filename, 'w', encoding='utf-8')
    file.write(data)
    file.close


def get_tags():
    tags = []
    for tag in config.TAGS:
        tags.append({'Key': tag, 'Value': config.TAGS[tag]})
    return tags


def create_ec2(userdata):
    client = boto3.resource('ec2')
    password = _create_password()
    script = read_whole_file(config.SCRIPT)
    script = script.replace('<PASSWORD>', password)
    sec_grp_id = read_file(config.SEC_GRP_FILE)
    instance = client.create_instances(
        ImageId=config.AMI_IMAGE,
        KeyName=config.KEY_NAME,
        InstanceType=config.INSTANCE_TYPE,
        MaxCount=1,
        MinCount=1,
        # NetworkInterfaces=[{
        #    'DeviceIndex': 0,
        #    'SubnetId': random.choice(config.SUBNETS),
        #    'Groups': [sec_grp_id],
        #    'AssociatePublicIpAddress': False
        # }],
        UserData=script,
        TagSpecifications=[{'ResourceType': 'instance', 'Tags': get_tags()}]
    )
    ec2_id = instance[0].id
    instance[0].wait_until_running()
    ec2_ip = instance[0].private_ip_address
    _write_ddb(ec2_id, ec2_ip, userdata, password)
    return ec2_ip, password


def _create_password():
    chars = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(chars)
                       for i in range(config.PASS_LENGTH))
    return password


def _write_ddb(ec2_id, ec2_ip, userdata, password):
    client = boto3.client('dynamodb')
    resp = client.put_item(
        TableName=config.DDB_TABLE,
        Item={
            'instanceid': {'S': ec2_id},
            'ip': {'S': ec2_ip},
            'cza': {'S': userdata[2]},
            'mail': {'S': userdata[5]},
            'password': {'S': password},

        }
    )
