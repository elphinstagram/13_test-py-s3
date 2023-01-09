import boto3

# instantiate a client
client = boto3.client('s3')

# retrieve all bucket Metadata
response = client.list_buckets()

# loop trough bucket data and display names
for b in response['Buckets']:
    print(b['Name'])
