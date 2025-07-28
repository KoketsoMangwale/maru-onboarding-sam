import json

def lambda_handler(event, context):
    tenant_id = event['tenantId']
    print(f"Provisioning for {tenant_id}...")
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Provisioned {tenant_id}'})
    }
