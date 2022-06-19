import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('KumiteFighters')

with open("fighters.json") as json_file:
    KumiteFighters = json.load(json_file)
    for fighter in KumiteFighters:
        Fighter = fighter['Fighter']
        Outfit = fighter ['Outfit']
        
        print("Adding Fighter:", Fighter, Outfit)

        table.put_item(
            Item={
                'Fighter': Fighter,
                'Outfit': Outfit,
            }
        )
        
