import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('KumiteFighters')


#Lambda use to query the table
def lambda_handler(event, context):
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('KumiteFighters')
    try:
        response = table.query(KeyConditionExpression=Key('Fighter').eq('1'))
    except:
        raise