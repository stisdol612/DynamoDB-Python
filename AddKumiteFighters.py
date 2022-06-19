import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('KumiteFighters')

with open("fighterdata.json") as json_file:
    Fighters = json.load(json_file)
    for fighters in Fighters:
        fighter = Fighter['fighter']
        outfit = Outfit ['outfit']
        
        print("Adding Fighter:", Fighter, Outfit)
        
        table.put_item(
            Item={
                'Fighter': Fighter,
                'Outfit' : Outfit
            }
        )