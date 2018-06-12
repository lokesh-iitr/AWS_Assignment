#!/bin/bash

aws ec2 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name KeyAssign1 --iam-instance-profile Name=PE_trainee_Admin_role --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Shell-assignment}, {Key=username,Value=Lokesh_Mahala},{Key=email_id,Value=lokesh.mahala@quantiphi.com}, {Key=Project,Value=PE_Training}]' --query Instances[0].InstanceId --user-data '#!/bin/bash 
aws s3 cp /home/lokesh/.ssh/id_rsa.pub s3://2017lokesh/id_rsa.pub' 

aws s3 ls s3://2017lokesh/id_rsa.pub

while [ $? -ne 0 ]
do 
    aws s3 ls s3://2017lokesh/id_rsa.pub
    if [[ $? -eq 0 ]]; then 
      echo "file found Go on"
      break
    else
      echo "please wait some tym" 
      sleep 20
    fi
done

aws ec2 run-instances --image-id ami-14c5486b --count 1 --instance-type t2.micro --key-name KeyAssign1 --security-group-ids --iam-instance-profile Name=PE_trainee_Admin_role --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Shell-assignment}, {Key=username,Value=Lokesh_Mahala},{Key=email_id,Value=lokesh.mahala@quantiphi.com}, {Key=Project,Value=PE_Training}]' --query Instances[0].InstanceId --user-data '#!/bin/bash 
aws s3 cp s3://2017lokesh/id_rsa.pub id_rsa.pub'