import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('KumiteFighters')

response = table.delete_item(Key = {'Fighter': 'Ray Jackson', 'Outfit': 'BlackSweats/GoldSash'})

print(response)