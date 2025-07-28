import json
import boto3

def lambda_handler(event, context):
    user_id = event['queryStringParameters']['user_id']
    boto3.client('events').put_events(Entries=[{
        'Source': 'maru.register',
        'DetailType': 'TenantRegistrationRequested',
        'Detail': json.dumps({"tenantId": user_id}),
        'EventBusName': 'default'
    }])
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Registered {user_id}'})
    }
