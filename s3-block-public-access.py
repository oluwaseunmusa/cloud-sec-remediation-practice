import boto3

def lambda_handler(event, context):
    # Specify the bucket name
    bucket_name = "YOUR_BUCKET_NAME"  # Replace with your bucket name

    # Create an S3 client
    s3 = boto3.client('s3')

    # Disable public access for the bucket
    try:
        response = s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print()
        print(f"====================================================")
        print(f"Public access disabled for bucket: {bucket_name} 🚀")
        print(f"====================================================")
        print()
        return {
            'statusCode': 200,
            'body': f"Public access disabled for bucket: {bucket_name} ❌"
        }
    except Exception as e:
        print()
        print(f"===================================")
        print(f"Error disabling public access: {e} ❌")
        print(f"===================================")
        print()
        return {
            'statusCode': 500,
            'body': f"Error disabling public access: {e}"
        }