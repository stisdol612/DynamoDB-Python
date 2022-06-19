import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('KumiteFighters')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Frank Dux",
            "Outfit" : "BlackGi/YellowSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Bolo Jenkins",
            "Outfit" : "BlackPants/RedSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Ray Jackson",
            "Outfit" : "BlackSweats/GoldSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Paco",
            "Outfit" : "Red Muy Thai Shorts"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Budimam Prang",
            "Outfit" : "BlackPants/YellowSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Chuan Ip Mung",
            "Outfit" : "GoldPants/YellowSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Attillio Reale",
            "Outfit" : "TealPants/GoldSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Pumola",
            "Outfit" : "Sumo Skirt"
        }
    )
    
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Sen Ling",
            "Outfit" : "GreyGi/RedSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            "Fighter": "Suan Paredes",
            "Outfit" : "BlueShorts/YellowSash"
        }
    )

with table.batch_writer() as batch:
    batch.put_item(
        Item={}
    )                                       

