import boto3

s3 = boto3.resource('s3')
bucket = s3.create_bucket(
    ACL='public-read-write',
    Bucket='checkingbuckgh',
    CreateBucketConfiguration=
        {
        'LocationConstraint': 'us-west-1'
        }
)

for i in s3.buckets.all():
        print(i.name)

