import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Kumite Fighters')

with table.batch_writer() as batch:
    batch.put_item(Item={"Fighter": "Frank Dux", "Outfit": "BlackGi/YellowSash"})
    batch.put_item(Item={"Fighter": "Bolo Jenkins", "Outfit": "BlackPants/RedSash"})
    batch.put_item(Item={"Fighter": "Ray Jackson", "Outfit": "BlackSweats/GoldSash"})
    batch.put_item(Item={"Fighter": "Paco", "Outfit": "Red Muy Thai Shorts"})
    batch.put_item(Item={"Fighter": "Budimam Prang", "Outfit": "BlackPants/YellowSash"})
    batch.put_item(Item={"Fighter": "Chuan Ip Mung", "Outfit": "GoldPants/YellowSash"})
    batch.put_item(Item={"Fighter": "Attillio Reale", "Outfit": "TealPants/GoldSash"})
    batch.put_item(Item={"Fighter": "Pumola", "Outfit": "Sumo Skirt"})
    batch.put_item(Item={"Fighter": "Sen Ling", "Outfit": "GreyGi/RedSash"})
    batch.put_item(Item={"Fighter": "Suan Paredes", "Outfit": "BlueShorts/YellowSash"})
print(batch)