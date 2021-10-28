import json
import boto3

# s3_client = boto3.client('s3')
dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table("CustomerDetails")

def lambda_handler(event, context):
    # TODO implement
    print(str(event))
    fname = event["fname"]
    lname = event["lname"]
    email = event["email"]
    password = event["pass"]
    contact = event["contact"]
    
    table.put_item(Item={
        "First Name":fname,
        "Last Name":lname,
        "EmailID":email,
        "Password":password,
        "Mobile No":contact
    })
    
    return 'Customer Added Successfully!'
