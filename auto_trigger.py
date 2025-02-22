import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def auto_trigger_handler(event, context):
    """
    Lambda function that gets triggered by DynamoDB stream events
    and prints the record ID to the console
    """
    try:
        # Log the entire event for debugging
        logger.info("Received event: %s", json.dumps(event))
        
        for record in event['Records']:
            # Ensure this is a new record (INSERT)
            if record['eventName'] == 'INSERT':
                # Get the DynamoDB record
                dynamodb_record = record['dynamodb']['NewImage']
                
                # Extract the ID from the record
                record_id = dynamodb_record['id']['S']
                
                # Log the ID
                logger.info(f"New record processed - ID: {record_id}")
                
                # You can add additional processing here if needed
                
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed DynamoDB stream event')
        }
        
    except Exception as e:
        logger.error(f"Error processing DynamoDB stream event: {str(e)}")
        raise e
