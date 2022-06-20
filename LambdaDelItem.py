import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('KumiteFighters')

def lambda_handler(event, context):
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('KumiteFighters')
    try:
        response = table.delete_item(Key = {'Fighter': 'Ray Jackson', 'Outfit': 'BlackSweats/GoldSash'})
        return "Done"
    except:
        raise
