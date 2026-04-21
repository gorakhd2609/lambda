import json
import boto3
from PIL import Image
import io
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

        response = s3.get_object(Bucket=bucket, Key=key)
        image_content = response['Body'].read()

        image = Image.open(io.BytesIO(image_content))
        image = image.convert("RGB")
        image = image.resize((100, 100))

        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)

        output_bucket = "myf1-resize"
        output_key = f"resized-{key.split('/')[-1]}"

        s3.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=buffer,
            ContentType='image/jpeg'
        )

        return {"status": "success"}

    except Exception as e:
        print("ERROR:", str(e))
        raise e
