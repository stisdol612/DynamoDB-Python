import boto3

dynamodb = boto3.resource('dynamodb')

#Lambda use to delete the table
def lambda_handler(event, context):
    client = boto3.resource('dynamodb')   
    table = client.table('KumiteFighters')    
    try:
     response = table.delete_table(TableName="KumiteFighters")
    except:
        raise
    
    print("You have successfully deleted the table.!")