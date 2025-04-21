import json
import boto3
import uuid
import traceback

textract = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

TABLE_NAME = 'InvoiceData'
TOPIC_ARN = 'arn:aws:sns:us-east-1:699475936750:InvoiceProcessedTopic'

def lambda_handler(event, context):
    try:
        print("✅ Event received:", json.dumps(event))

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"📂 File triggered from bucket: {bucket}, key: {key}")

        response = textract.analyze_document(
            Document={'S3Object': {'Bucket': bucket, 'Name': key}},
            FeatureTypes=["FORMS"]
        )

        extracted_text = ''
        for block in response['Blocks']:
            if block['BlockType'] == 'LINE':
                extracted_text += block['Text'] + '\n'

        print("📝 ExtractedText:\n" + extracted_text)

        invoice_id = str(uuid.uuid4())
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            'InvoiceID': invoice_id,
            'FileName': key,
            'ExtractedText': extracted_text
        })
        print("✅ Data saved to DynamoDB")

        sns_response = sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='Invoice Processed',
            Message=f'Invoice {key} processed and stored with ID {invoice_id}'
        )
        print("📧 SNS email sent successfully. Message ID:", sns_response['MessageId'])

        return {
            'statusCode': 200,
            'body': json.dumps('Invoice processed successfully!')
        }

    except Exception as e:
        print("❌ Exception occurred:")
        traceback.print_exc()
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
