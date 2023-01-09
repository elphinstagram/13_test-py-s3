import os
import boto3

# instantiate a client
client = boto3.client('s3')

# set variables
target_bucket = 's3-sachiko-aws3'
current_path = os.getcwd()
target_file = 'test_upload.csv'
target_filepath = os.path.join(current_path, 'downloads', target_file)

# object method to download file
client.download_file(
    Bucket=target_bucket,
    Key=target_file,
    Filename=target_filepath
)

# list the content of DL dir
downloads_dir = os.path.join(current_path, 'downloads')

for root, dirs, files in os.walk(downloads_dir):
    for fn in files:
        print(fn)
