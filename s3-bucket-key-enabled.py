import boto3
import json

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Specify the bucket name
    bucket_name = 'your-bucket-name'
    
    try:
        # Enable Bucket Key for the specified bucket
        response = s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'aws:kms',
                            'BucketKeyEnabled': True
                        }
                    }
                ]
            }
        )
        print()
        print(f"====================================================")
        print(f"Bucket Key enabled for bucket: {bucket_name} 🚀")
        print(f"====================================================")
        print()
        return {
            'statusCode': 200,
            'body': json.dumps(f'Bucket Key enabled for bucket: {bucket_name}')
        }
    except Exception as e:
        print()
        print(f"====================================================")
        print(f"Error enabling Bucket Key: {str(e)} ❌")
        print(f"====================================================")
        print()
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error enabling Bucket Key: {str(e)}')
        }