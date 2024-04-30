import json

def lambda_handler(event, context):
    name = event['name']
    message = f"Hello, {name}!"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
