import json
import base64
import boto3

from datetime import datetime

def lambda_handler(event, context):

    client = boto3.client('dynamodb')

    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        t_record = base64.b64decode(record['kinesis']['data'])

        # decode the bytes into a string
        str_record = str(t_record,'utf-8')

        #transform the json string into a dictionary
        dict_record = json.loads(str_record)


        # Create app Row
        #############################
        
        user_key = dict()
        user_key.update({'user_id': {"N": str(dict_record['user_id'])}}) #partion Key
        #user_key.update({'event_id': {"S": str(dict_record['event_id'])}}) #sort key
        #create export dictionary
        ex_dynamoRecord = dict()

        #remove user_id, user_information and app_id from dynmodb record
        app_dict = dict(dict_record)
        app_dict.pop('user_id',None)
        app_dict.pop('app_id',None)
        #app_dict.pop('user_details',None)

        #turn the dict into a json
        app_json = json.dumps(app_dict)

        #create a record (column) for the user_id
        
        #ex_dynamoRecord.update({str(dict_record['user_details']): {'Value':{"S":app_json},"Action":"PUT"}})
        ex_dynamoRecord.update({str(dict_record['app_id']): {'Value':{"S":app_json},"Action":"PUT"}})
        

        #print(ex_dynamoRecord)
        response = client.update_item(TableName='users_app_data_dynamoDB', Key = user_key, AttributeUpdates = ex_dynamoRecord)


    return 'Successfully processed {} records.'.format(len(event['Records']))
    
    

      

