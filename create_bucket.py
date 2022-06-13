import logging
import boto3

from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    
    """
    Create a new S3 bucket, default region is us-east-1    
    
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

while True:

    name_for_bucket = input('Please input a name for the bucket: ')
    region = input('Input a region (default us-east-1): ')

    if create_bucket(name_for_bucket, region):
        print("Bucket has been created!")
    else:
        print("Bucket has not been created")
    
