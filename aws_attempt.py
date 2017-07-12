import boto3
aws_access_key_id = 'Your Key'
aws_secret_access_key = 'Your Secret Key'


def checkinstance(aws_access_key_id,aws_secret_access_key):
    instances = []
    regions = ['sa-east-1','us-east-2c']

    for region in regions:
        rds = boto3.client('ec2',region_name=region)
        result = rds.describe_instances()
        instances.append(result)

    return(current_instances)

checkinstance(aws_access_key_id,aws_secret_access_key)
