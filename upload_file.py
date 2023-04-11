import json
import boto3
import base64
import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(f"event: {event}")
    get_file_content = event['body']
    
    
    decoded_content = base64.b64decode(get_file_content)
    
     # Generate unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.jpg"
    
    s3_upload = s3.put_object(Bucket='photo-storing-bucket', Key=filename, Body=decoded_content)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('File uploaded successfully')
    }
