DATA_FILE = 'export_users.csv'
SEC_GRP = 'LD-sec-grp'
SEC_GRP_FILE = 'secgrp'
AMI_IMAGE = 'ami-0e00e602389e469a3'
INSTANCE_TYPE = 't2.micro'
SCRIPT = 'userdata.sh'
PASS_LENGTH = 10
DDB_TABLE = 'LD-table'
KEY_NAME = 'LD-key'
KEY_FILE = 'key'
SUBNETS = ['subnet-0cd7259af1bc788d4',
           'subnet-029bf33b29c4d99c5', 'subnet-0ae7e9bc300b9988d']
TAGS = {
    'environment': 'Dev',
    'confidentiality': '2 - General',
    'application-id': 'DAAS',
    'application-name': 'learning-desktops',
    'cost-center': 'C0013050',
    'team': 'Cloud Administrators',
    'product-project': 'learning-desktops',
    'product-owner': 'cloud-admins@rb.cz',
    'shared-services': 'false',
    'entity': 'RBCZ'
}
