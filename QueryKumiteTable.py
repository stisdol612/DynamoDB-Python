import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Kumite Fighters')

response = table.query(KeyConditionExpression=Key('Fighter').eq('Chong Li'))

for item in response['Items']:
    print(item)