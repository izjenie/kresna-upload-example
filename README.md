# Kresna File Uploader

A serverless application for uploading files to AWS S3 with metadata stored in DynamoDB.

## Prerequisites

1. Node.js and npm installed
2. AWS Account and AWS CLI configured
3. Serverless Framework installed (`npm install -g serverless`)
4. Python 3.9 or higher

## AWS Setup Required

1. AWS Account with appropriate permissions
2. AWS Access Key and Secret Key with the following permissions:
   - AWSLambdaFullAccess
   - AmazonS3FullAccess
   - AmazonDynamoDBFullAccess
   - AmazonAPIGatewayAdministrator
   - IAMFullAccess

## Installation

1. Install Serverless Framework:
```bash
npm install -g serverless
```

2. Configure AWS credentials:
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your preferred region (e.g., ap-southeast-1)
# Enter output format (json)
```

3. Install project dependencies:
```bash
pip install -r requirements.txt
```

4. Deploy the application:
```bash
serverless deploy
```

## Project Structure

- `serverless.yml` - Serverless Framework configuration
- `handler.py` - Lambda functions
- `public/index.html` - Frontend upload form
- `requirements.txt` - Python dependencies
