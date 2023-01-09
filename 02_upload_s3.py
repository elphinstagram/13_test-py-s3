import boto3
import os

# instantiate a client
client = boto3.client('s3')

# set variables
target_bucket = 's3-sachiko-aws3'
current_path = os.getcwd()
target_file = 'test_upload.csv'
target_filepath = os.path.join(current_path, 'data', target_file)

# open the file
data = open(target_filepath, 'rb')

# load data into S3
client.upload_file(target_filepath, target_bucket, target_file)
