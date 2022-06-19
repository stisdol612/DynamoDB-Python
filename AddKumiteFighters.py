import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('KumiteFighters')

with open("fighters.json") as json_file:
    Fighters = json.load(json_file)
    for fighters in Fighters:
        Fighter = ['Frank Dux']
        Outfit = ['BlackGi/YellowSash']
        
        print("Adding Fighter:")
        
        table.put_item(
            Item={
                'Fighter': 'Frank Dux'
                'Outfit' : 'BlackGi/YellowSash'
            }
        )     