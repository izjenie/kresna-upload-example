from auto_trigger import auto_trigger_handler

# Sample DynamoDB stream event
test_event = {
    'Records': [
        {
            'eventName': 'INSERT',
            'dynamodb': {
                'NewImage': {
                    'id': {'S': 'test-123'},
                    'filename': {'S': 'test.txt'},
                    'text': {'S': 'Sample text'}
                }
            }
        }
    ]
}

# Call the handler with our test event
print("Testing auto_trigger_handler with sample event...")
result = auto_trigger_handler(test_event, None)
print(f"\nHandler response: {result}")
