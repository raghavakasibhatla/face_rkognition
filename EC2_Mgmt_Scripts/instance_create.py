import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
     ImageId='',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )
