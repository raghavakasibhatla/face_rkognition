import boto3

client = boto3.client('ec2',region_name='us-west-2') #Add your region

print('Loading function')

def lambda_handler(event, context):
    responses = client.start_instances(
    InstanceIds=[
        'YOUR INSTANCE IDs'
    ],

    DryRun=True # Make it False to test
)
