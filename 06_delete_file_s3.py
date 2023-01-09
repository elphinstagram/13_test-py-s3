import boto3

# instantiate a client
client = boto3.client('s3')

# set variables
target_bucket = 's3-sachiko-aws3-new'

# List all objects in bucket
all_objects = client.list_objects(Bucket=target_bucket)

# print the contents
print(f"List of obj in {target_bucket}:")
for a in all_objects['Contents']:
    print(a['Key'])


def del_file(filename):
    client.delete_object(
        Bucket=target_bucket,
        Key=filename
    )


# cli message
print('\nList of files to be deleted:')

for a in all_objects['Contents']:
    if 'example/' in a['Key'] and a['Key'] != 'example/':
        print(f"file to be deleted {a['Key']}")
        del_file(a['Key'])

print("Deletion Processed")

# Refresh object metadata
all_objects = client.list_objects(Bucket=target_bucket)

# print the contents
print(f"List of obj in {target_bucket}:")
for a in all_objects['Contents']:
    print(a['Key'])
