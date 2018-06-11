import boto3
def lokesh(event, context):
    # TODO implement
    s3 = boto3.resource('s3')
    key = event['Records'][0]['s3']['object']['key'] #find the key of our file 
    copy_source = {
        'Bucket': 'lokesh2018',
        'Key': key
        }
    destination_bucket = s3.Bucket('2017lokesh')  #destination bucket
    destination_bucket.copy(copy_source, 'destinationkey') #copy file from our source bucket and paste into destination bucket 