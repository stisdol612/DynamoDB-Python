import boto3
#Create DynamoDB Table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName ='KumiteFighters',
    KeySchema = [
        {
            'AttributeName': 'Fighter',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Outfit',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'Fighter',
            'AttributeType': 'S' 
        },
        {
            'AttributeName': 'Outfit',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print(table)
