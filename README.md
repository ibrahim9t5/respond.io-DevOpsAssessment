# respond.io-DevOpsAssessment

Prequisites

Install Python3,
Install and Configure AWS CLI,
Install AWS SAM CLI,

Step 1
create Lambda Function using SAM

Step 2
create trigger for Lambda when new object added in S3 bucket, you can verify trigger by going to S3Bucke/Properties/EventNotfications

Step 3
lambda function that 1: Check if file is zip or not, 2: if not, download file in temp, 3: will convert it to zip, 4: Upload file to s3
and 5: Delete older file from S3 bucket

Step 4
Create Custom Role and Permission for Lambda function to get,put and delete obj from S3 bucket

TASK 2
Create S3 Bucket that will have Json Video Files and Connect with LAMBDA in same Template File

To run this project run:
sam deploy --capabilities CAPABILITY_NAMED_IAM (in terminal)