# Serverless_application
This repo contains the source code for AWS lambda function i.e. **s3_json_dynamodb_lambda**.

**Language used : Python**

**AWS Services used : API Gateway, S3, Lambda, DynamoDB and CodeBuild**

1. There is **Customer Registration Form** which takes the input from the User.
2. Once the user clicks on Register button, it will generate the API call.
3. This **POST API call** is handled by **AWS API Gateway** service and publish the details of the customer to the **AWS DynamoDB** using **Lambda** Service.
4. The source code files for the form are stored in **AWS S3** Bucket.
