import json
import boto3
import os
import uuid
import base64
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def upload_handler(event, context):
    try:
        # Parse multipart form data
        body = json.loads(event['body'])
        file_content_base64 = body['file']
        description = body['description']
        file_name = body['fileName']
        
        # Decode base64 file content
        file_content = base64.b64decode(file_content_base64)
        
        # Generate unique ID
        file_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        
        # Upload to S3
        s3_key = f"{file_id}/{file_name}"
        s3.put_object(
            Bucket=os.environ['BUCKET_NAME'],
            Key=s3_key,
            Body=file_content,
            ContentType='application/octet-stream'
        )
        
        # Save metadata to DynamoDB
        item = {
            'id': file_id,
            'fileName': file_name,
            'description': description,
            's3Key': s3_key,
            'timestamp': timestamp
        }
        
        table.put_item(Item=item)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            'body': json.dumps({
                'message': 'Upload successful',
                'fileId': file_id
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True,
            },
            'body': json.dumps({
                'error': str(e)
            })
        }

def process_upload(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            file_id = record['dynamodb']['NewImage']['id']['S']
            print(f"New file uploaded with ID: {file_id}")
            # You can add additional processing here
