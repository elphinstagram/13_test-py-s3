import boto3

# client instance
client = boto3.client('s3')

# variables
target_bucket = "s3-sachiko-aws3"
subfolder01 = 'examples/'
subfolder02 = 'test_folder/'

# create subfolder (objects)
client.put_object(Bucket=target_bucket, Key=subfolder01)
client.put_object(Bucket=target_bucket, Key=subfolder02)

# retrieve object info from bucket
all_objects = client.list_objects(Bucket=target_bucket)

# iterate through Metadata and list objects
for a in all_objects['Contents']:
    print(a['Key'], a['LastModified'])
