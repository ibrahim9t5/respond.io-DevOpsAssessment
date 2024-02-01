import json
import os
import boto3
import zipfile

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('HI I am Lambda!')
    }