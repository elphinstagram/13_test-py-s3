import boto3

# instantiate a client
client = boto3.client('s3')

# set the new bucktname
new_bucket = 's3-sachiko-aws3-new3'

# create new bucket
client.create_bucket(
    Bucket=new_bucket,
    CreateBucketConfiguration={"LocationConstraint": "ap-northeast-1"}
)

# retrieve all bucket Metadata
response = client.list_buckets()

# loop trough bucket data and display names
for b in response['Buckets']:
    print(b['Name'])
