import boto3
import json
print ("Something")
def erro(event):
    print ("Event is ",event)
    client = boto3.client('lambda')
    response = client.invoke(
    FunctionName= 'erro',
    InvocationType='Event',
    Payload=json.dumps(event))  
    
    print ("Response is ",response)
    return 'Hello Quantiphi'




event = {
  "id": 101,
  "firstname": "ramesh",
  "designation": "developer"
}

print("Output is ",erro(event))

#In Asynchronous invocations event are queued before they are invoked and if the execution fails, 
#they are retried twice with delays between invocations. 
#Type Of Error 
#Timeout Error
#Out Of Memory Exception
#Configuration Failure