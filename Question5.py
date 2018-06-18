In this problem we divide our work in 2 sections 
1. First is frontend work
2. Second is backend work


First we start with our frontend :-
In this section first we create our simple webpage using HTML,CSS. On this page we have a login page section .
In our problem  our user is divided in two part first is HR and second is employee.

If employee use our webpage then he/she can only view the list of all employee
If HR use our webpage then he/she can view all the employee details and can edit the details

In technical term employee use GET httpmethod or HR can use GET,POST,PUT,Delete httpdmethod.

After creating simple webpage we create a AWS S3 bucket for hosting our webpage. In bucket we can see a property called host a static website. In this property we just define our index.html page name and we receive a URL for our webpage from here 

Authentication using Amazon Cognito Service

In this first we create user pool in cognito service and store our user pool id 
From user pool we select app client and store user app client id 
In S3 bucket we store a file config.js In this file just update our user pool id or user app client id 
In this service we can remove our signup page

In this section we create backend part
First we create DyanamoDB Table for storing and retrieving our data
In this table we have two column id or name 

Now we create our lambda function this function triggered when we hit our API


import boto3

db_res = boto3.resource("dynamodb")
def lambda_handler(event, context):
    
    #
    table_detail = get_response_from_dynamo_table('lokesh')
    item_count = table_detail['Count']
    item_list = table_detail['Items']
    
    print("Event",event)
    for  i in range(item_count):
        print("",item_list[i])
    add_item('lokesh',event)
    
    return event["http_method"]
    
    
  #after calling this function we get whole dynamo db table  
def get_response_from_dynamo_table(tb_name):
    tb_detail = db_res.Table(tb_name)#get table details using table name 
    response = tb_detail.scan() #scan whole table
    return response #return whole response 

#this method add item into our table 
def add_item(tb_name,event_dic):
    tb_detail = db_res.Table(tb_name) #get table details 
    response = tb_detail.put_item(Item = event_dic) #put our item in table using put_item function
    return response

def del_item(tb_name,pk_name,pk_value):
    tb_detail = db_res.Table(tb_name) #get table details 
    response = tb_detail.delete_item(Key={pk_name:pk_value}) #delete our item in table usign primary key name or value 
    return response
