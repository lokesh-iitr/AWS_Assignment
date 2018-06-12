


import boto3
region = 'us-east-1'
instances = ['i-07251d008a83940f5']

def Start_EC2_Instance(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print ('your  instances started: ' + str(instances))



import boto3
region = 'us-east-1'
instances = ['i-07251d008a83940f5']

def Stop_EC2_Instance(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print ('your  instances stopped: ' + str(instances))