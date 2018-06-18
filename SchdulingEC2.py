
#part1
#first client enter start or stop schedule time using shell script file 

#shell script file 
echo "Please enter start schedule time"
read start 
echo "Please enter stop schedule time"
read stop

#after entering start and stop time we just call cronjobscheduler lambda function 
aws lambda invoke --function-name 'cronjoblokesh' --invocation-type 'Event' --payload '{"start":"$start","stop":"$stop"}' outputfile.txt 

#part2
#Now we see our scheduler lambda function body 
import boto3
import datetime


def cronjobschedule(event, context):
    
    ec2=boto3.client('ec2')
    currenttime = datetime.datetime.now()
    id =  'i-07251d008a83940f5'
    region = 'us-east-1'

    #from event dictionary we just split schedule starting hour of our instance 
    startScheduleTime=[(int(x) for x in event['start'].split())]
    #from event dictionary we just split schedule stoping hour of our instance 
    stopScheduleTIme=[(int(x) for x in event['stop'].split())]
    
    
    #if our current time is in between default schedule time and new schedule time then we have to stop our instance 
    if 9<currenttime.hour<startScheduleTime[0]: 
        response=ec2.stop_instances(InstanceIds=id, region_name=region)
        
    #if our current time is greator then new schedule time but less then default schedule time then we have to start our instance 
    elif startScheduleTime[0]<currenttime.hour<9:
        response=ec2.start_instances(InstanceIds=id, region_name=region)
    #if our new schedule time is less then default schedule time then we to start our instance 
    elif startScheduleTime[0]<9<currenttime.hour:
        response=ec2.start_instances(InstanceIds=id, region_name=region)
    #if our current time is greator then defult sechedule time or less then new schedule time then we have to start our instance 
    if 18<currenttime.hour<stopScheduleTIme[0]:
        response=ec2.start_instances(InstanceIds=id, region_name=region)
    #if our current time is less default schedule time or greator then new schedule time then we have to stop our instance    
    elif stopScheduleTIme[0]<currenttime.hour<18:
        response=ec2.stop_instances(InstanceIds=id, region_name=region)
    


    client1=boto3.client('events')
    response = client1.put_rule(
        Name='StartEC2',
        ScheduleExpression='cron(0 %s ? * MON-FRI *)' %(start[0]),
        State='ENABLED',
        Description='Start ec2 instance on schedule time'
    )
    response1 = client1.put_rule(
        Name='StopEc2',
        ScheduleExpression='cron(0 %s ? * MON-FRI *)' %(stop[0]),
        State='ENABLED',
        Description='Stops ec2 instance on schedule time '
    )

#part3
#lambda function for starting our instance

import boto3
region = 'us-east-1'
instances = ['i-07251d008a83940f5']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print ('your  instances started: ' + str(instances))

#part4
#lambda function to stop our ec2 instance
import boto3
region = 'us-east-1'
instances = ['i-07251d008a83940f5']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print ('your  instances stopped: ' + str(instances))

