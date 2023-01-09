import boto3

# instantiate client
client = boto3.client('s3')

# var
target_bucket = 's3-sachiko-aws3-new'

# retrieve the bucket list
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])

# delete bucket
client.delete_bucket(
    Bucket=target_bucket
)

print('\nRemaining Buckets:')

# retrieve the bucket list(after delete)
response = client.list_buckets()

for n in response['Buckets']:
    print(n['Name'])
