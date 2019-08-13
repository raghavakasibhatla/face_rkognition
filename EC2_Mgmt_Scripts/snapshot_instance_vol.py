import boto3

response = client.create_snapshot(
    Description='string',
    VolumeId='vol-0ae8a32f38e2a35da',
    TagSpecifications=[
        {
            'ResourceType':'instance'
                'Tags': [
                {
                    'Key': 'flask',
                    'Value': 'flask'
                },
            ]
        },
    ],
    DryRun=True|False
)
