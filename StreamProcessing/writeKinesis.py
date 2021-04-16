import json
import boto3

def lambda_handler(event, context):

    print("MyEvent:")
    print(event)
    method = event['context']['http-method']
    # method = event['http-method']
    print ("method IS", method)
    if method == "GET":
        dynamo_client = boto3.client('dynamodb')
        # im_user_id = event['params']['querystring']['user_id']
        print('user_id is', im_user_id)
        response = dynamo_client.get_item(TableName = 'users_app_data_dynamoDB', Key = {'user_id':{'N': im_user_id}})
        print('requested item is :', response['Item'])
        # response_category = response['category']
        # response_user_age = response['user_age']
        
        
        #myreturn = "This is the return of the get"

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
           }

    elif method == "POST":

        p_record = event['body-json']
        print('p_record',p_record)
        recordstring = json.dumps(p_record)
        print('recordstring',recordstring)

        client = boto3.client('kinesis',region_name='us-east-1', endpoint_url='https://kinesis.us-east-1.amazonaws.com/')
        response = client.put_record(
            StreamName='firstKinesis',
            Data= recordstring,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }