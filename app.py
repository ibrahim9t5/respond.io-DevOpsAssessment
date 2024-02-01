import json
import os
import io
import tempfile
import zipfile
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Check if the file is not already a zip file
        if not key.endswith('.zip'):
            compressed_key = f"{os.path.splitext(key)[0]}.zip"
            source_file_path = download_from_s3(bucket, key)
            zip_content = compress_to_zip(source_file_path)
            upload_to_s3(bucket, compressed_key, zip_content)
            print(f"File compressed and uploaded: {bucket}/{compressed_key}")

            # Delete the original file from S3
            delete_from_s3(bucket, key)
            print(f"Original file deleted: {bucket}/{key}")

    return {
        'statusCode': 200,
        'body': json.dumps('Process completed successfully!')
    }

def download_from_s3(bucket, key):
    local_file_path = f'/tmp/{os.path.basename(key)}'
    s3.download_file(bucket, key, local_file_path)
    return local_file_path

def compress_to_zip(source_file_path):
    zip_content = io.BytesIO()
    with zipfile.ZipFile(zip_content, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(source_file_path, os.path.basename(source_file_path))

    zip_content.seek(0)
    return zip_content.read()

def upload_to_s3(bucket, key, content):
    s3.put_object(Body=content, Bucket=bucket, Key=key)

def delete_from_s3(bucket, key):
    s3.delete_object(Bucket=bucket, Key=key)